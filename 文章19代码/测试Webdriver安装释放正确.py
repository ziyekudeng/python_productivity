from selenium import webdriver
import time

'''
webdriver下载地址:
chrome http://npm.taobao.org/mirrors/chromedriver
edge   https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

安装路径 C:\Users\高巍\AppData\Local\Programs\Python\Python39\Scripts
'''

browser =  webdriver.Edge()

browser.get("http://www.jd.com")

# 等待10秒
time.sleep(10)

content = browser.page_source
print(content)

browser.quit()