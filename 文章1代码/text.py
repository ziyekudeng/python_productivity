from time import struct_time
import xlrd
import xlwt
from pathlib import Path,PurePath

src_path='python_productivity\文章1代码\调查问卷\调查问卷模版.xlsx'
dst_file='python_productivity\文章1代码\result'

p=Path(src_path)
files=[x for x in p.iterdir() if PurePath(x).match('*.xls')]

content=[]

for file in files:
    username=file.stem
    date=xlrd.open_workbook(file)
    table=date.sheet()[0]