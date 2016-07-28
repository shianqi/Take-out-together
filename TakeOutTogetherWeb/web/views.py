from web.tool import json_tool
from django.http import HttpResponse
from web.crawler import baidu_crawler
from web.tool import loc_tool

# Create your views here.
def index(request):

    list = baidu_crawler.get_shop_list(0,0)
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