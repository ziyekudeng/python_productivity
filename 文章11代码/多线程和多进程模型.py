'''
多进程的并行计算更适用于计算密集型应用，即程序运行过程中主要为计算类 CPU 开销大的程序

多线程模型适合 I/O 密集型的应用
'''


# 多进程模型
from multiprocessing import Pool

# 多线程模型
from multiprocessing.dummy import Pool

# multiprocessing.dummy的Pool用法和multiprocessing库相同