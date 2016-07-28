import httplib2
import re
from web.crawler.shop_info import Shop_info
from web.tool import meituan_tool

def get_shop_list(lat, lng):
    data = meituan_tool.post(lat, lng)
    data = data.replace('false', '0')
    data = data.replace('true', '1')
    # print(data)
    data = eval(data)
    shops = data.get('poilist')
    shop_info_list = []
    for shop in shops:
        shop_info = Shop_info()
        shop_info.shop_name = shop.get('name')
        shop_info.native_url = 'meituanwaimai://waimai.meituan.com/menu?restaurant_id=' + str(shop.get('id')) + '&poiname='
        shop_info.deliver_time = shop.get('avg_delivery_time')
        shop_info.distance = shop.get('distance')
        shop_info.logo_url = shop.get('pic_url_square')
        shop_info.take_out_cost = shop.get('shipping_fee')
        shop_info.take_out_price = shop.get('min_price')
        discounts = shop.get('discounts2');
        for discount in discounts:
            if discount.get('type') == 6:
                discount_msg = discount.get('info')
                discount_str_list = re.findall(r"\d+\.?\d*", discount_msg)
                discount_list = []
                for discount_str in discount_str_list:
                    discount_list.append(int(discount_str))
                shop_info.welfare = discount_list
                shop_info.source = 'meituan'
                shop_info_list.append(shop_info)
    return shop_info_list


