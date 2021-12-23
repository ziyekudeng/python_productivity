from time import struct_time
import xlrd
from pathlib import Path,PurePath

file = 'result/结果.xlsx'
data = xlrd.open_workbook(file)
table = data.sheets()[0]
value = table.cell_value(rowx=1,colx=1)

src_path = '11/11'

p = Path(src_path)
files = [x for x in p.iterdir() if PurePath(x).match('*.xlsx')]

