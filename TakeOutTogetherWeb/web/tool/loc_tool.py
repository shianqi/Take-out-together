import httplib2
# 地理位置模块
# 1：GPS设备获取的角度坐标，wgs84坐标;
#
# 2：GPS获取的米制坐标、sogou地图所用坐标;
#
# 3：google地图、soso地图、aliyun地图、mapabc地图和amap地图所用坐标，国测局坐标;
#
# 4：3中列表地图坐标对应的米制坐标;
#
# 5：百度地图采用的经纬度坐标;
#
# 6：百度地图采用的米制坐标;
#
# 7：mapbar地图坐标;
#
# 8：51地图坐标




def gaode_to_baidu09mc(lat,lng):
    baidu_map_key = 'ULEiGSyEImEElBdV0slGAHVn7bB6QmME'
    baidu_map_url = 'http://api.map.baidu.com/geoconv/v1/?coords={coords}&from={from}&to={to}&ak={ak}'
    coords = str(lat) + ',' + str(lng)
    baidu_map_url = baidu_map_url.replace('{coords}', coords)
    baidu_map_url = baidu_map_url.replace('{from}', str(3))

    baidu_map_url = baidu_map_url.replace('{to}' , str(6))

    baidu_map_url = baidu_map_url.replace('{ak}', baidu_map_key)


    http = httplib2.Http()
    url = baidu_map_url
    body = ''
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.2.0'}
    response, content = http.request(url, method='GET', headers=headers)
    content = content.decode('utf-8')
    content = eval(content)
    try:
        x = content.get('result')[0].get('x')
        y = content.get('result')[0].get('y')
        return x,y
    except:
        return '0','0'

def gaode_to_baidu09ll(lat,lng):
    baidu_map_key = 'ULEiGSyEImEElBdV0slGAHVn7bB6QmME'
    baidu_map_url = 'http://api.map.baidu.com/geoconv/v1/?coords={coords}&from={from}&to={to}&ak={ak}'
    coords = str(lat) + ',' + str(lng)
    baidu_map_url = baidu_map_url.replace('{coords}', coords)
    baidu_map_url = baidu_map_url.replace('{from}', str(3))

    baidu_map_url = baidu_map_url.replace('{to}' , str(5))

    baidu_map_url = baidu_map_url.replace('{ak}', baidu_map_key)


    http = httplib2.Http()
    url = baidu_map_url
    body = ''
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.2.0'}
    response, content = http.request(url, method='GET', headers=headers)
    content = content.decode('utf-8')
    content = eval(content)
    try:
        x = content.get('result')[0].get('x')
        y = content.get('result')[0].get('y')
        return x,y
    except:
        return '0','0'