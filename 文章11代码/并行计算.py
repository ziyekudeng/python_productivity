from multiprocessing import Pool,Queue
import os
import psutil


# 逻辑cpu个数
count = psutil.cpu_count()

# 定义一个队列用于存储进程id
queue = Queue()

# 用于计算平方和将运行函数的进程id写入队列
def f(x):
    queue.put(os.getpid())
    return x*x

'''
windows下使用multiprocessing，要将进程池相关代码应该放在if __name__ == '__main__'下面，要不然运行会报错
'''
def test():
    with Pool(count) as p:
        # 并行计算
        res = p.map(f, range(1, 1001))
        print(f'计算平方的结果是:{res}')

if __name__ == '__main__':
    test()

# 并行计算用到的进程id
pids = set()
while not queue.empty():
    pids.add(queue.get())

print(f'用到的进程id是: {pids}')
