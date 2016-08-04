
from web.tool.img_tool import img_shrink
from web.crawler import baidu_crawler,meituan_crawler,ele_crawler,meituan_web_crawler

def get_shop_list(lat,lng,source):
    list = []

    try:
        if source.find('baidu') >= 0:
            list_baidu = baidu_crawler.get_shop_list(lng, lat)
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

    list.sort(key=lambda x: (x.weight))
    list.reverse()
    return list