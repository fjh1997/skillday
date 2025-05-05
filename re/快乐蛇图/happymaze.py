import dis
import marshal
import sys
from hashlib import md5

# 迷宫地图 (10x10)
# 0=路径, 1=墙, S=起点, E=终点
MAZE = [
    "1S11111111",
    "1001000001",
    "1101011111",
    "1001010001",
    "1011010101",
    "1010010101",
    "1011110101",
    "1000000101",
    "1111101101",
    "1111100E11"
]

def validate_path(path):
    """验证迷宫路径是否正确"""
    x, y = 0, 1  # 起点位置 (第0行, 第1列)
    visited = set()
    
    for move in path:
        # 记录访问位置
        if (x, y) in visited:
            return False
        visited.add((x, y))
        
        # 移动处理
        if move == 'U':
            x -= 1
        elif move == 'D':
            x += 1
        elif move == 'L':
            y -= 1
        elif move == 'R':
            y += 1
        else:
            return False  # 非法移动
        
        # 检查边界和墙壁
        if x < 0 or y < 0 or x >= 10 or y >= 10:
            return False
        if MAZE[x][y] == '1':
            return False
        
        # 检查是否到达终点
        if MAZE[x][y] == 'E':
            return True
    
    return False

def generate_flag(path):
    """根据正确路径生成flag"""
    if not validate_path(path):
        return "Wrong path! Try again."
    
    # 使用路径和特定盐值生成flag
    salt = "pyRev3rs3"
    flag_base = f"CTF{{Maze_{path}_{salt}}}"
    flag_hash = md5(flag_base.encode()).hexdigest()
    return f"flag{{Maze_{flag_hash[:16]}}}"

def main():
    print("=== Maze Escape Challenge ===")
    print("Find the correct path through the maze!")
    print("Valid moves: U (Up), D (Down), L (Left), R (Right)")
    
    while True:
        path = input("Enter your path: ").strip().upper()
        result = generate_flag(path)
        print(result)
        
        if not result.startswith("Wrong"):
            break

if __name__ == "__main__":
    main()