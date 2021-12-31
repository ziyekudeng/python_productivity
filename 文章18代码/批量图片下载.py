from requests_html import HTMLSession

# URL
name = "猫"
url = f"https://unsplash.com/s/photos/{name}"

# 启动
session = HTMLSession()

# GET请求
result = session.get(url)

# 结果
print(result.status_code)

'''

<head>
</head>
<body>
    <div num=1>
        <figure itemprop="image">
           ... ...
           <div num=2> 
              ... ...  
              <a rel="nofollow" href=http://...>
              ... ...
           </div>
        </figure>
    </div>
</body>
'''


down_list = result.html.xpath('//figure[@itemprop="image"]//a[@rel="nofollow"]/@href')

# 'https://unsplash.com/photos/24FBpjv3XVI/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8MXx8JUU3JThDJUFCfHwwfHx8fDE2NDA4ODg1NjU&force=true'

def get_picID_from_url(url):
    return url.split('&force')[0].split('?ixid=')[1]

def down_one_pic(url):
  result = session.get(url)
  filename = get_picID_from_url(url) + '.jpg'
  with open(filename, "wb") as f:
    f.write(result.content)
 
for one_url in down_list:
    down_one_pic(one_url)
    