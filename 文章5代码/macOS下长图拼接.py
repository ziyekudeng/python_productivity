from pathlib import Path, PurePath
from subprocess import run

'''
安装ImageMagick软件，安装参考博客：https://blog.csdn.net/qq_37674858/article/details/80361860）：
'''

jpg_path = 'data/ch04'
result_path = 'data/ch04/result.jpg'


p = Path(jpg_path)

# 增加命令
cmd = ["composite",]

# 增加参数
for x in p.iterdir() if  PurePath(x).match('*.jpg'):
    cmd.append(x)

# 增加结果
cmd.append(result_path)

run(cmd)