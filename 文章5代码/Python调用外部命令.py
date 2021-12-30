from subprocess import run, Popen, PIPE

'''
run() 函数:执行一个新的程序，\把第一个参数指定为要执行程序的路径就可以了。如果要执行的程序带有参数，那就可以使用列表数据类型存放可执行程序名称和参数.
ls命令在运行的时候需要环境变量，而环境变量是存在于shell中的。所以需要增加shell=True。
'''
cmd1 = ["ls", "."]
returncode = run('ls', '.', shell=True)

print(returncode)
# CompletedProcess(args=['ls', '.'], returncode=0)
# returncode是“ls .”的退出状态码.
# 通常来说, 一个为 0 的退出码表示进程运行正常

# 使用Popen获取程序运行结果
with Popen(cmd1, shell=True, stdout=PIPE, stderr=PIPE, encoding="utf-8") as fs:
    fs.wait(2)
    
    # 从标准输出中读取数据,知道文件结束
    files = fs.communicate()[0]

print(files)
