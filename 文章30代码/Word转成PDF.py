from win32com import client
import os
'''
pywin32  支持 Office 所有组件的库,只能运行在windows系统上

安装包 pip3 install pypiwin32
导入库 import win32com
'''
def word2pdf(filepath, wordname, pdfname):
    worddir = filepath
    # 指定Word类型
    word = client.DispatchEx("Word.Application")
    # 使用Word软件打开a.doc
    file = word.Documents.Open('\\'.join([worddir, wordname]), ReadOnly=1)
    # 文件另存为当前目录下的pdf文件
    file.ExportAsFixedFormat('\\'.join([worddir, pdfname]), ExportFormat=17, 
                             Item=7, CreateBookmarks=0)
    # 关闭文件
    file.Close()
    # 结束word应用程序进程   
    word.Quit()


if __name__ == "__main__":
    # 获取当前文件的父目录
    father_path = os.path.abspath(os.getcwd())

    file_path = '\\'.join([father_path, 'python_productivity\文章30代码\样例'])
    word_name = '计算机软件著作权完成人证明.docx'
    pdf_name = '计算机软件著作权完成人证明.pdf'

    word2pdf(file_path, word_name, pdf_name)

