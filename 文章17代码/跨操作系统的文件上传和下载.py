import os
from flask import Flask, request

'''
1.执行命令
python3 -m http.server 8080
通过在命令行运行这行代码之后，就能通过“http:// 你的 IP 地址:8080”浏览和下载文件了。

2.参考文档:
http://docs.jinkan.org/docs/flask/patterns/fileuploads.html
'''

app = Flask(__name__)

#使用了相对路径的写法，将上传目录指定成了“当前执行命令的目录”
app.config['UPLOAD_FOLDER'] = os.getcwd()

html = '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

'''
函数的装饰器，它的作用是在不改变被装饰函数的内容的前提下，给函数增加新的功能，装饰器也是由函数实现的，它的语法格式是在装饰器前增加一个“@”符号。
'''
@app.route('/', methods=['GET', 'POST'])
# 要把内存中的数据保存到文件
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
