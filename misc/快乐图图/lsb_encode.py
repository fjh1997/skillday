from PIL import Image
import numpy as np

def text_to_binary(text):
    """将文本转换为二进制字符串"""
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    """将二进制字符串转换回文本"""
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return text

def encode_lsb(image_path, text, output_path):
    """将文本隐写到图片中"""
    # 打开图片并转换为numpy数组
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # 将文本转换为二进制
    binary_text = text_to_binary(text)
    binary_text += '1111111111111110'  # 添加结束标记
    
    # 检查图片是否能容纳文本
    max_bits = img_array.size * 3  # 每个像素有3个通道(RGB)
    if len(binary_text) > max_bits:
        raise ValueError("文本太长，无法隐写到这张图片中")
    
    # 隐写过程
    data_index = 0
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):  # RGB三个通道
                if data_index < len(binary_text):
                    # 修改最低有效位
                    img_array[i, j, k] = (img_array[i, j, k] & 0xFE) | int(binary_text[data_index])
                    data_index += 1
                else:
                    break
    
    # 保存隐写后的图片
    encoded_img = Image.fromarray(img_array)
    encoded_img.save(output_path)
    print(f"隐写完成，结果已保存到 {output_path}")

def decode_lsb(image_path):
    """从图片中提取隐藏的文本"""
    # 打开图片并转换为numpy数组
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # 提取LSB位
    binary_data = []
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):  # RGB三个通道
                binary_data.append(str(img_array[i, j, k] & 1))
    
    # 将二进制数据转换为字符串
    binary_str = ''.join(binary_data)
    
    # 查找结束标记
    end_index = binary_str.find('1111111111111110')
    if end_index == -1:
        raise ValueError("未找到隐藏的文本或图片未被隐写")
    
    # 提取有效二进制数据并转换为文本
    binary_text = binary_str[:end_index]
    text = binary_to_text(binary_text)
    
    return text

# 使用示例
if __name__ == "__main__":
    # 隐写示例
    input_image = "original.png"  # 原始图片路径
    output_image = "encoded.png"  # 隐写后图片路径
    secret_text = "flag{h@pPY_9RaNdpan1U}"  # 要隐藏的文本
    
    # 执行隐写
    encode_lsb(input_image, secret_text, output_image)
    
    # 提取示例
    extracted_text = decode_lsb(output_image)
    print("提取的隐藏文本:", extracted_text)