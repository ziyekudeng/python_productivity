from win32com import client
import os
'''
pywin32  支持 Office 所有组件的库,只能运行在windows系统上

安装包 pip3 install pypiwin32
导入库 import win32com
'''

def excel2pdf(filepath, excelname, pdfname):
    exceldir = filepath
    # 指定Excel类型
    excel = client.DispatchEx("Excel.Application")
    # 使用Excel软件打开a.xls
    # 注意乱码:以标准open调用为例，open(filename,encoding=utf8)
    file = excel.Workbooks.Open('\\'.join([exceldir, excelname]), False)
    # 文件另存为当前目录下的pdf文件
    file.ExportAsFixedFormat(0, '\\'.join([exceldir, pdfname]))
    # 关闭文件
    file.Close()
    # 结束excel应用程序进程   
    excel.Quit()


if __name__ == "__main__":
    # 获取当前文件的父目录
    father_path = os.path.abspath(os.getcwd())

    file_path = '\\'.join([father_path, 'python_productivity\文章30代码\样例'])
    wordname ='工作表.xlsx'
    pdfname ='工作表'
    excel2pdf(file_path, wordname, pdfname)