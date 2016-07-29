from web.tool import json_tool
from django.http import HttpResponse
from web.crawler import baidu_crawler,meituan_crawler
from web.tool import loc_tool
from django.shortcuts import render_to_response
from web.tool.weight_tool import weight_cal

# Create your views here.
def index(request):
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')

    lat , lng = 111.688879,40.814422

    print(float(lat))
    print(float(lng))

    list = baidu_crawler.get_shop_list(lat,lng)
    list1 = meituan_crawler.get_shop_list(lng,lat)
    print(len(list1))
    list.extend(list1)

    for shop_info in list:
        shop_info.weight = weight_cal(shop_info)

    list.sort(key=lambda  x:(x.weight))
    list.reverse()

    json_str = json_tool.class_to_json(list)

    return HttpResponse(json_str, content_type="application/json")

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