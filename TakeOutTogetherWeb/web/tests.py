from django.test import TestCase

import time
import httplib2
from web.tool.loc_tool import gaode_to_baidu
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
               'User-Agent': 'okhttp/3.2.0','Cookie':'uuid=..0.0.0; oc=--; abt=1454175307.0%7CACE; iuuid=; ioc=--; ci=191; webp=1; poiid=1218741; _ga=GA1.2.1578715842.1469542721; w_addr=; w_visitid=; wx_channel_id=0; terminal=i; w_utmz="utm_campaign=(direct)&utm_source=0&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_uuid=9ee53e87-af66-443a-a3ff-5c504b9c587a; utm_source=0; w_cid=; w_cpy_cn=""; w_cpy=huhehaote; w_geoid=wrr2jt8vyrgv; w_latlng=40812492,111688315; JSESSIONID=; __mta=....21'}
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
    print(len(data))
    print(result)

print(gaode_to_baidu('111.688927','40.81443'))