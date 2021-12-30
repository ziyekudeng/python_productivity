import xlrd
from pathlib import Path, PurePath
from collections import defaultdict
from collections import Counter

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
    sheet = xlrd.open_workbook(file)

    # 遍历表格
    for table in  sheet.sheets():
        # 从第二行遍历内容
        for line in range(1,table.nrows):
            fruit = table.row_values(rowx=line, start_colx=0, end_colx=None)

            # 统计每种水果的销售额           
            fruit_name = dict_trans_chi2eng(fruit[0])[0]
            total[fruit_name] = total[fruit_name] + fruit[-2]

    # 每张表格是一个月份,进行一次月份统计之后,将临时统计清零
    # 用每个excel的文件名区分月份

    # 提取文件名 在Path对象上查看name属性path.name。如果不想带后缀，可以查看stem属性path.stem。
    print(f"月份为: {file.stem} 本月水果销量 Top3为:")

    # 排序并取出Top3
    # 通过sort函数排序取出Top3也可以实现
    #  这里我直接使用Counter函数
    '''
    Counter 包支持对列表和字典进行排序、数量统计、取前 n 个数的功能，非常强大。
    '''
    sorted_total = Counter(total)

    # 清空本月统计数据
    total = defaultdict(int)
    '''
    在排序之后，提取前 N 个元素的问题，
    '''
    print(sorted_total.most_common(3))
