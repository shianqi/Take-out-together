from web.tool import json_tool
from django.http import HttpResponse
from web.crawler import baidu_crawler,meituan_crawler,ele_crawler
from web.tool import loc_tool
from django.shortcuts import render_to_response
from web.tool.weight_tool import weight_cal

# Create your views here.
def index(request):
    # lat lng 为经纬度
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    # 经纬度
    source = request.GET.get('source')
    source = str(source)
    lat , lng = 111.688879,40.814422
    source = 'baidu,meituan,eleme'
    print(float(lat))
    print(float(lng))
    list = []
    if  source.find('baidu') >=0:
        list_baidu = baidu_crawler.get_shop_list(lat, lng)
        list.extend(list_baidu)
    if source.find('meituan') >=0:
        list_meituan = meituan_crawler.get_shop_list(lng, lat)
        list.extend(list_meituan)
    if source.find('eleme') >=0:
        list_ele = ele_crawler.get_shop_list(lng, lat)
        list.extend(list_ele)


    for shop_info in list:
        shop_info.weight = weight_cal(shop_info)

    list.sort(key=lambda  x:(x.weight))
    list.reverse()

    json_str = json_tool.class_to_json(list)
    response = HttpResponse(json_str, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response
# GET /public/common/toolbar/css/index.css HTTP/1.1
# Host: c.csdnimg.cn
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
# Accept: text/css,*/*;q=0.1
# Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
# Accept-Encoding: gzip, deflate
# Referer: http://blog.csdn.net/fanyuna/article/details/5568089
# Connection: keep-alive
# If-Modified-Since: Mon, 16 Nov 2015 10:38:49 GMT
# Cache-Control: max-age=0


def loc(request):
    lat = 111.695549
    lng = 40.8205
    result1 = loc_tool.gcj02tobd09(lng, lat)
    result2 = loc_tool.bd09togcj02(lng, lat)
    result3 = loc_tool.wgs84togcj02(lng, lat)
    result4 = loc_tool.gcj02towgs84(lng, lat)
    result5 = loc_tool.geocode('北京市朝阳区朝阳公园')
    print (result1, result2, result3, result4, result5)
    return HttpResponse('hello world')

def t(request):
    return render_to_response('tiaozhuan.html')