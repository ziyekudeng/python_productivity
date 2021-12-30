import pathlib 

file_name = "需要统计字数.txt"

# 取得脚本所在目录
# __file__必须在使用 python xxx.py 的形式运行才能正确得到python脚本文件的完整路径
current_path = pathlib.PurePath(__file__).parent
print('脚本所在目录')
print(current_path)

# 和脚本同目录下的文件绝对路径
file = current_path.joinpath(file_name)
print('和脚本同目录下的文件绝对路径')
print(file)

# Python 中的 with 语句用于异常处理，封装了 try…except…finally 编码范式
# macOS 系统文字的编码为 UTF-8 编码，Windows 下为 GB2312 编码。
with open(file, encoding='utf8') as f:

    content = f.read()
    # rstrip() 函数，自动剔除出现在文件末尾的空行、空格
    words = content.rstrip()
    number = len(words)
    print(number)
    # 15

# with open("统计结果.txt", "w", encodong="utf-8") as f:
# f.write("15个字符")


