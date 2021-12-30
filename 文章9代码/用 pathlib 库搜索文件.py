from pathlib import Path

'''
glob() 函数可以实现基于文件名的搜索方法
rglob 函数可以实现基于扩展名的搜索方法。
'''

base_dir = 'python_productivity\文章1代码\调查问卷'
keywords = '**/*模版*'

# 遍历base_dir指向的目录下所有的文件
p = Path(base_dir)

# 当前目录下包含模版的所有文件名称
files = p.glob(keywords)  
# files的类型是迭代器
# 通过list()函数转换为列表输出
print(list(files))

# xlsx结尾的文件
files2 = p.rglob('*.xlsx')
print(list(files2))


# 遍历子目录和所有文件
files3 = p.glob('**/*')
print(list(files3))
