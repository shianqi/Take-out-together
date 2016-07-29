import httplib2
from web.tool.meituan_tool import encodeGeo
from web.crawler import shop_info

def get_shop_list(lat, lng):
    url = 'https://m.ele.me/restapi/v4/restaurants?type=geohash&geohash={geohash}1&offset=0&limit=20&extras[]=food_activity&extras[]=restaurant_activity'
    url = url.replace('{geohash}', encodeGeo(lat, lng))
    http = httplib2.Http();
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.2.0'}
    response, content = http.request(url, method='GET', headers=headers)
    content = content.decode('utf-8')
    content = eval(content)
    print(content)
