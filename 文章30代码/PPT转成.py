from win32com import client
import os
'''
pywin32  支持 Office 所有组件的库,只能运行在windows系统上

安装包 pip3 install pypiwin32
导入库 import win32com
'''

def ppt2pdf(filepath, pptname, pdfname):
    pptdir = filepath
    # 指定PPT类型
    ppt = client.DispatchEx("PowerPoint.Application")
    # 使用ppt软件打开a.ppt
    file = ppt.Presentations.Open('\\'.join([pptdir, pptname]), False)
    # 文件另存为当前目录下的pdf文件
    file.ExportAsFixedFormat('\\'.join([pptdir, pdfname]), FixedFormatType=2, 
                             PrintRange=None)
    # 关闭文件
    file.Close()
    # 结束excel应用程序进程   
    ppt.Quit()


if __name__ == "__main__":
    # 获取当前文件的父目录
    father_path = os.path.abspath(os.getcwd())

    file_path = '\\'.join([father_path, 'python_productivity\文章30代码\样例'])
    wordname ='演示文稿.pptx'
    pdfname ='演示文稿.pdf'
    ppt2pdf(file_path, wordname, pdfname)