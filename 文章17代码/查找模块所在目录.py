
# $ python3
import http
import sys

print(f'模块所在目录:{http.__file__}')

# 模块所在目录:C:\Users\高巍\AppData\Local\Programs\Python\Python39\lib\http\__init__.py

print(f'Python模块保存目录:{sys.path}')


'''
执行结果:
Python模块保存目录:['d:\\work_research_python\\python_productivity\\文章17代码', 'C:\\Users\\高巍\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 'C:\\Users\\高巍\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 'C:\\Users\\高巍\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\Users\\高巍\\AppData\\Local\\Programs\\Python\\Python39', 'C:\\Users\\高巍\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages']
'''