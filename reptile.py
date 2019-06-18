from multiprocessing import Process
import requests
import re
import DB.MySqlHelper
proxies = {
  "http": "http://203.202.248.35:8080",
  "http": "http://109.172.51.162:35783",
}

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
}

r = requests.get("https://www.baidu.com/baidu?wd=kk&tn=monline_4_dg&ie=utf-8", headers=headers, verify=False)
pattern = re.compile(r'href="([a-zA-z]+://[^\s]*)"')
#print(r.text)
url = re.findall(pattern, r.text)
print(url)
for i in url:
  print(i)
#print(url[0].split('"'))
print(len(url))