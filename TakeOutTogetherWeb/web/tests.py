from django.test import TestCase

import time
import httplib2
# Create your tests here.
print(int(time.time()*1000))

def decode(data):
    stepLength  = (len(data) & 7) + 1
    result = ''
    for i in range(len(data)):
        result = result + str(int(data[i]) - stepLength)
    return result

def meituan_post():
    http = httplib2.Http()
    url = 'http://i.waimai.meituan.com/home?lat=40.812492&lng=111.688315'
    body = 'page_index=0&apage=1'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.2.0'}
    response, content = http.request(url, method='POST', body=body, headers=headers)
    # content = content.decode('utf-8')
    content = eval(content)
    data = content.get('data')
    stepLength = (len(data) & 7) + 1
    result = ''
    for i in range(len(data)):
        print(chr(ord(data[i])-stepLength))
        result += str(chr(ord(data[i])-stepLength))
    # print(decode(content.get('data')))
    print(result)
meituan_post()