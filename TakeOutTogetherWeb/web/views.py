from web.tool import json_tool
from django.http import HttpResponse
from web.crawler import baidu_crawler,meituan_crawler,ele_crawler,meituan_web_crawler
from web.tool import loc_tool
from django.shortcuts import render_to_response
from web.tool.weight_tool import weight_cal
from web.tool.img_tool import img_shrink
# Create your views here.
def index(request):
    # lat lng 为经纬度
    lng = request.GET.get('lng')
    lat = request.GET.get('lat')
    # 经纬度
    source = request.GET.get('source')

    list = []



    try:
        if  source.find('baidu') >=0:
            list_baidu = baidu_crawler.get_shop_list(lng , lat)
            for shop_info in list_baidu:
                shop_info.logo_url = img_shrink(shop_info.logo_url, shop_info.shop_id)
            list.extend(list_baidu)
    except:
        print('baidu except')
        pass

    try:
        if source.find('meituan') >= 0:
            list_meituan = meituan_web_crawler.get_shop_list(lat, lng)
            for shop_info in list_meituan:
                shop_info.logo_url = img_shrink(shop_info.logo_url, shop_info.shop_id)
            list.extend(list_meituan)
    except:
        print('meituan except')
        pass

    try:
        if source.find('eleme') >= 0:
            list_ele = ele_crawler.get_shop_list(lat, lng)
            list.extend(list_ele)
    except:
        print('ele except')
        pass





    list.sort(key=lambda  x:(x.weight))
    list.reverse()

    json_str = json_tool.class_to_json(list)
    response = HttpResponse(json_str, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"

    return response




def t(request):
    return render_to_response('tiaozhuan.html')