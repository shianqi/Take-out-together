import httplib2
from web.crawler.shop_info import Shop_info
import time
from web.tool import loc_tool,weight_tool
import re

def get_shop_list(lat, lng):
    lat = str(lat)
    lng = str(lng)
    request_time = str(int(time.time()*1000))
    lat, lng = loc_tool.gaode_to_baidu09mc(lat,lng)

    http = httplib2.Http()
    url = 'http://client.waimai.baidu.com/shopui/na/v1/cliententry?resid=1001&from=na-android&os=5.1.1&sv=3.9.1&cuid=E8E7DA5EEF8BD6A7BEE5918C36C96DDD%7C273344620823668&model=2014813&screen=720*1280&channel=com.xiaomi&loc_lat={lat}&loc_lng={lng}&city_id=&aoi_id=&address=&net_type=wifi&isp=46007&request_time={request_time}'

    url = url.replace('{request_time}',request_time)
    url = url.replace('{lat}',str(lng))
    url = url.replace('{lng}',str(lat))


    body = 'lat=0.0&lng=0.0&count=50&page=1&bduss=NA&stoken=bdwm&sortby=&taste=&city_id=&promotion=&return_type=launch'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.2.0'}
    response, content = http.request(url, method='POST', body=body, headers=headers)
    content = content.decode('utf-8')
    content = eval(content)
    # print(content.get('result').get('shop_info')[0].get('shop_name'))
    shops = content.get('result').get('shop_info')
    shop_info_list = []
    for shop in shops:
        shop_info = Shop_info()
        shop_info.source_img = './img/bd.png'
        shop_info.web_url = 'http://waimai.baidu.com/mobile/waimai?qt=shopmenu&is_attr=1&shop_id=' + str(shop.get('shop_id'))
        shop_info.score = shop.get('average_score')
        shop_info.month_sale_num = shop.get('saled_month')
        shop_info.shop_name = shop.get('shop_name')
        shop_info.native_url = shop.get('bdwm_url').replace('\\','').replace('\\','')
        shop_info.deliver_time = shop.get('delivery_time')
        shop_info.distance = shop.get('distance')
        shop_info.logo_url = shop.get('logo_url')[0:69].replace('\\','')
        shop_info.take_out_cost = shop.get('takeout_cost')
        shop_info.take_out_price = shop.get('takeout_price')
        shop_info.shop_id = 'BD' + shop.get('shop_id')
        # 计算折扣信息
        welfare_str_list = []
        welfare_act_infos = shop.get('welfare_act_info')
        for welfare_act_info in welfare_act_infos:
            if welfare_act_info.get('type') == 'jian':
                welfare_msg = welfare_act_info.get('msg')
                welfare_str_list = re.findall(r"\d+\.?\d*",welfare_msg)

        welfare_list = []

        for i in range(int(len(welfare_str_list)/2)):
            temp_welface_list = []
            x = int(welfare_str_list[i*2])
            y = int(welfare_str_list[i*2+1])
            temp_welface_list.append(x)
            temp_welface_list.append(y)
            welfare_list.append(temp_welface_list)
        shop_info.welfare = welfare_list
        shop_info.source = 'baidu'
        shop_info.weight= weight_tool.weight_cal(shop_info.welfare,shop_info.take_out_price,shop_info.take_out_cost)
        shop_info_list.append(shop_info)
    return shop_info_list