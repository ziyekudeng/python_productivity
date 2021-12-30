from pathlib import Path, PurePath
from subprocess import run

'''
Windows下的长图拼接代码示例（安装ImageMagick软件，安装参考博客)：https://blog.csdn.net/qq_37674858/article/details/80361860）：
'''

jpg_path = 'python_productivity\文章5代码\图片'
result_path = 'python_productivity\文章5代码\图片\result.jpg'
p = Path(jpg_path)


# 使用命令
cmd = ['magick', 'convert', '-append']

# 增加参数
for x in p.iterdir():
    if PurePath(x).match('*.jpg'):
        cmd.append(x)
    
# 增加拼接结果
cmd.append(result_path)

print(cmd)

run(cmd, shell=True)