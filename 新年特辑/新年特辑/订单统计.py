import xlrd
from pathlib import Path, PurePath
from collections import defaultdict

# 订单路径
download_path = 'python_productivity\新年特辑\新年特辑\订单'

# 取得该目录下所有的xlsx格式文件
p = Path(download_path)
files = [x for x in p.iterdir() if PurePath(x).match('*.xlsx')]

# 定义字典用于结果统计
'''
这里的defaultdict(function_factory)构建的是一个类似dictionary的对象，其中keys的值，自行确定赋值，但是values的类型，是function_factory的类实例，而且具有默认值。
比如default(int)则创建一个类似dictionary对象，里面任何的values都是int的实例，而且就算是一个不存在的key, d[key] 也有一个默认值，这个默认值是int()的默认值0.
'''
total = defaultdict(int)

# 中文做字典的key会有问题,做两个简单的翻译函数
tran_dict =  {
    "dragon_fruit":"火龙果",
    "coconut":"椰子",
    "watermelon":"西瓜"
}
# 中文翻译成英文
def dict_trans_chi2eng(value):
    return [k for k,v in tran_dict.items() if v == value]

# 英文翻译成中文
def dict_name_eng2chi(key):
    return tran_dict[key]

# 遍历文件 
for file in files:
    # 也可以用openpyxl代替xlrd打开.xlsx文件：
    # df=pandas.read_excel(‘data.xlsx’,engine=‘openpyxl’)
    sheet = xlrd.open_workbook(file)

    # 遍历表格
    for table in  sheet.sheets():
        # 从第二行遍历内容
        for line in range(1,table.nrows):
            fruit = table.row_values(rowx=line, start_colx=0, end_colx=None)
            # 第一列水果名称, 倒数第二列销售金额
            # print(f'{fruit[0]},{fruit[-2]}')
            # 火龙果,15.0
            # 椰子,16.0
            # 西瓜,10.5

            # 统计每种水果的销售额           
            fruit_name = dict_trans_chi2eng(fruit[0])[0]
            # print(fruit_name)
            # print(total[fruit_name])
            # print(total)
            total[fruit_name] = total[fruit_name] + fruit[-2]

for fruit_name in total:
    print(f'水果: {dict_name_eng2chi(fruit_name)} , 总金额: {total[fruit_name]}')

    # 水果: 火龙果 , 总金额: 135.0
    # 水果: 椰子 , 总金额: 144.0
    # 水果: 西瓜 , 总金额: 94.5