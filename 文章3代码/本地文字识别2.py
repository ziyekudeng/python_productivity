import pytesseract
from PIL import Image

'''
第一步，图像输入；
第二步，前期处理，比如二值化，图像降噪，倾斜纠正；
第三步，文字检测，比如版面分析，字符分割；
第四步，文本识别，比如字符识别，后期矫正；
第五步，也就是最后一步，输出文本。

问题: pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH. See README file for more information.
报错解决: pytesseract是依赖c++编写的tesseract工具才能正常工作的，tesseract的下载地址是 
https://github.com/tesseract-ocr
https://github.com/UB-Mannheim/tesseract/wiki
'''

# 打开图片
image = Image.open('python_productivity\\文章3代码\\样例图片\\example.png')

# 转为灰度图片
imgry = image.convert('L')

# 二值化，采用阈值分割算法，threshold为分割点,根据图片质量调节
threshold = 150
table = []
for j in range(256):
    if j < threshold:
        table.append(0)
    else:
        table.append(1)

temp = imgry.point(table, '1')

# OCR识别：lang指定中文,--psm 6 表示按行识别，有助于提升识别准确率
text = pytesseract.image_to_string(temp, lang="chi_sim+eng", config='--psm 6')

# 打印识别后的文本
print(text)