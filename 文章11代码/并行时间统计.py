from multiprocessing import Pool
import os
import time
import psutil


# 逻辑cpu个数
count = psutil.cpu_count()


# 用于计算平方
def f(x):
    return x*x

'''
windows下使用multiprocessing，要将进程池相关代码应该放在if __name__ == '__main__'下面，要不然运行会报错
'''

def test():
    with Pool(count) as p:
        # 并行计算
        time1 = time.time()
        res = p.map(f, range(1, 1001))
        time2 = time.time()
        print(f'计算平方的结果是:{res}')

if __name__ == '__main__':
    test()


print(str(time2-time1))
