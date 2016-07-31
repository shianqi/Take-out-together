from web.tool.meituan_tool import encodeGeo
from httplib2 import Http
from web.crawler.shop_info import Shop_info
from web.tool import weight_tool

def get_shop_list(lat,lng):
    http = Http()
    url = 'http://waimai.meituan.com/ajax/poilist'
    body = 'classify_type=cate_all&sort_type=0&price_type=0&support_online_pay=0&support_invoice=0&support_logistic=0&page_offset=1&page_size=20'
    cookie = str(encodeGeo(lat,lng))
    cookie = 'w_geoid=' + cookie
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.2.0', 'Cookie': cookie}
    response, content = http.request(url, method='POST', body=body, headers=headers)

    content = content.decode('utf-8')
    content = content.replace('true','1')
    content = content.replace('false', '0')
    content = content.replace('null', '0')
    shops = eval(content).get('data').get('poiList')
    shop_info_list = []
    for shop in shops:
        shop_info = Shop_info()
        shop_info.source_img = './img/mt.png'
        shop_info.shop_name = shop.get('wmPoi4Web').get('name')
        shop_info.native_url = 'meituanwaimai://waimai.meituan.com/menu?restaurant_id=' + str(shop.get('wmPoi4Web').get('wm_poi_id')) + '&poiname='
        shop_info.deliver_time = shop.get('wmPoi4Web').get('avg_delivery_time')
        shop_info.distance = 0
        shop_info.logo_url = shop.get('wmPoi4Web').get('pic_url')
        shop_info.take_out_price = shop.get('wmPoi4Web').get('wmCPoiLbs').get('min_price')
        shop_info.take_out_cost = shop.get('wmPoi4Web').get('wmCPoiLbs').get('shipping_fee')
        shop_info.source = 'meituan'
        shop_info.shop_id = 'MT' + str(shop.get('wmPoi4Web').get('wm_poi_id'))
        shop_info.month_sale_num = shop.get('wmPoi4Web').get('month_sale_num')
        shop_info.score = shop.get('wmPoi4Web').get('wm_poi_score')
        discount_detail_list = shop.get('actInfoVo').get('full_discount_logo')
        if discount_detail_list == 0:
            continue
        discount_detail_list = discount_detail_list.get('discount_detail')
        welfare_list = []
        for discount_detail in discount_detail_list:
            temp_welfare = []
            x = discount_detail.get('limit_price')
            y = discount_detail.get('discount')
            temp_welfare.append(x)
            temp_welfare.append(y)
            welfare_list.append(temp_welfare)
        shop_info.welfare = welfare_list
        shop_info.weight = weight_tool.weight_cal(shop_info.welfare, shop_info.take_out_price, shop_info.take_out_cost)
        shop_info_list.append(shop_info)
    return shop_info_list