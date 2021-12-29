from aip import AipOcr

""" 你的 APPID AK SK """
# APP_ID = '你的 App ID'
# API_KEY = '你的 Api Key'
# SECRET_KEY = '你的 Secret Key'

# 识别应用
APP_ID = ''
# 识别用户
API_KEY = ''
# 加密密钥
SECRET_KEY = ''

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
# 参数：图片的路径和名称

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('python_productivity\文章3代码\样例图片\example.png')

""" 调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(image)

print('%s %s' % ('调试信息: ', result))

info = []
for i in result['words_result']:
    info.append(i['words'])
print(info)

with open('result.txt', 'w') as f:
    f.write(str(info))






# """ 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()

# image = get_file_content('example.jpg')

# """ 调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image);

# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"

# """ 带参数调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image, options)

# url = "https//www.x.com/sample.jpg"

# """ 调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url);

# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"

# """ 带参数调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url, options)


# {
# "log_id": 2471272194,
# "words_result_num": 2,
# "words_result":
#     [
#         {"words": " TSINGTAO"},
#         {"words": "青島睥酒"}
#     ]
# }
