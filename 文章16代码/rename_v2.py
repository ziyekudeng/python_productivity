import os
import argparse

'''
该程序需要使用   python3 脚本名称.py  方式执行
'''

'''
批量改名函数
file_path: 批量改名的路径
old_ext: 要修改的文件扩展名
'''
def rename(file_path, old_ext):

    print(old_ext)
    old_names = os.listdir(file_path)
    new_name = 1

    for old_name in old_names:

        if old_name.endswith(old_ext):

            old_path = os.path.join(file_path, old_name)
            new_path = os.path.join(file_path, str(new_name)+".JPG")
            os.rename(old_path, new_path)
            new_name = int(new_name)+1

def args_opt():
    '''
    获取命令行参数函数
    '''

    #定义参数对象
    parser = argparse.ArgumentParser()
    # 增加参数选项、是否必须、帮助信息
    parser.add_argument("-p", "--path", required=True, help="path to rename")
    parser.add_argument("-e", "--ext", required=True, help="files name extension, eg: jpg")
    # 返回取得的所有参数
    return  parser.parse_args()


if __name__ == "__main__":

    # args 对象包含所有参数，属性是命令行参数的完整名称
    args = args_opt()
    # 调用重命名函数，将命令行参数作为重命名函数的参数
    print(f'args.path:{args.path}')
    print(f'args.ext:{args.ext}')
    rename(args.path, "."+args.ext)
    # 输出改名之后的结果
    print(os.listdir(args.path))
    #  ['3.JPG', '2.JPG', '1.JPG', 'xyz.bmp']

# python3 rename_v2.py -p python_productivity\文章16代码\样例图片 -e jpg