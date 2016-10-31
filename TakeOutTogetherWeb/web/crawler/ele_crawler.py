import httplib2
from web.tool.meituan_tool import encodeGeo
from web.crawler.shop_info import Shop_info
import re
from web.tool import weight_tool

def get_shop_list(lat, lng):
    url = 'https://m.ele.me/restapi/v4/restaurants?type=geohash&geohash={geohash}1&offset=0&limit=50&extras[]=food_activity&extras[]=restaurant_activity'
    url = url.replace('{geohash}', encodeGeo(lat, lng))
    http = httplib2.Http();
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.2.0'}
    response, content = http.request(url, method='GET', headers=headers)
    content = content.decode('utf-8')
    content = str(content)
    content = content.replace('true', '1')
    content = content.replace('false', '0')
    content = content.replace('null', '0')
    # print(content)

    content = eval(content);
    logo_url = 'https://fuss10.elemecdn.com{url}?imageMogr/quality/75/format/jpg/thumbnail/!96x96r/gravity/Center/crop/96x96/'
    native_url = 'eleme://restaurant?restaurant_id={id}&animation_type=1'
    shop_info_list = []
    for shop in content:
        shop_info = Shop_info()
        shop_info.source_img = './img/elm.png'
        shop_info.web_url = 'https://m.ele.me/shop/' + str(shop.get('id'))
        shop_info.score = shop.get('rating')
        shop_info.month_sale_num = shop.get('month_sales')
        shop_info.shop_id = 'ELE' + str(shop.get('id'))
        shop_info.shop_name = shop.get('name')
        shop_info.native_url = native_url.replace('{id}', str(shop.get('id')))
        shop_info.deliver_time = shop.get('order_lead_time')
        shop_info.distance = shop.get('distance')
        shop_info.logo_url = logo_url.replace('{url}', shop.get('image_path'))
        shop_info.take_out_cost = shop.get('delivery_fee')
        shop_info.take_out_price = shop.get('minimum_order_amount')
        discounts = shop.get('restaurant_activity');
        for discount in discounts:
            if discount.get('type') == 102:
                discount_msg = discount.get('description')
                discount_str_list = re.findall(r"\d+\.?\d*", discount_msg)
                discount_list = []
                for i in range(int(len(discount_str_list) / 2)):
                    temp_welface_list = []
                    x = int(discount_str_list[i * 2])
                    y = int(discount_str_list[i * 2 + 1])
                    temp_welface_list.append(x)
                    temp_welface_list.append(y)
                    discount_list.append(temp_welface_list)
                shop_info.welfare = discount_list
                shop_info.source = 'eleme'
                shop_info.weight = weight_tool.weight_cal(shop_info.welfare, shop_info.take_out_price, shop_info.take_out_cost)
                shop_info_list.append(shop_info)
    return shop_info_list


