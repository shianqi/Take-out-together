import httplib2
import re
import web.crawler.shop_info

def get_shop_list(lat, lng):
    http = httplib2.Http();
    lat = int(lat * 1000000)
    lng = int(lng * 1000000)
    lat = str(lat)
    lng = str(lng)
    url = 'http://waimaiapi.meituan.com/api/v6/poi/filter?utm_medium=android&utm_content=866328026443372&utm_term=40604&utm_source=1011&ci=139&utm_campaign=AwaimaiBwaimaiGhomepage&uuid=AFF2123C2D6E56EBBA147FAA0A114A2FA3124CC425AF486E01FE6FA4ECB370F8&__vhost=api.waimai.meituan.com&__skck=6a375bce8c66a0dc293860dfa83833ef&__skts=1469690167201&__skua=d41d8cd98f00b204e9800998ecf8427e&__skno=d58e5c03-5b7e-40c8-9583-00f0bbc139ca&__skcy=XL5euL4GCvxgeOTU6LGzS5dznLE%3D'
    body = 'wm_logintoken=&poilist_mt_cityid=139&wm_actual_longitude=' + lng + '&wm_actual_latitude=' + lat + '&req_time=1469690167244&last_wm_poi_id=0&trace_tag=%7B%22action%22%3A%22pull_down%22%2C%22src_page%22%3A%22p_homepage%22%2C%22src_block%22%3A%22b_pull_down%22%2C%22tgt_page%22%3A%22p_homepage%22%2C%22req_time%22%3A%221469690167256%22%2C%22tgt_block%22%3A%22%5B%5C%22b_poilist%5C%22%5D%22%7D&wm_did=866328026443372&userid=0&wm_longitude=111689245&wm_channel=1011&poilist_wm_cityid=150100&sort_type=0&page_size=20&push_token=8068bb1e75bd379905e34a7e931cd59ae31fa9d6c876fcbaa3a4e3e410dfe5ea103b4d6d4a8cb7a6cd70f822f26ffff9&load_type=2&category_type=0&navigate_type=0&wm_appversion=4.6.4&wm_latitude=40814457&waimai_sign=oP6Ggaz8Y%2F877XkVNlZGcaRro3E9nyc1znh2IhZsQmV36S6rXTbdtEShskl8aIPVk79EX%2BfJRECDLOkNGJe65veZ3%2FvPSvRT91caUpLWubrSfXJ0AQ8DOLGDAiWV%2F25kblOOsF9tGuy1nn3f2LF%2BqpzMIFOv0%2F1fZ0D0qfZrDCs%3D&longitude=111689245&wm_ctype=android&second_category_type=0&wm_visitid=d19d1f25-7092-41a1-8c96-1a60f33e0f06&wm_dversion=22_5.1.1&wm_uuid=AFF2123C2D6E56EBBA147FAA0A114A2FA3124CC425AF486E01FE6FA4ECB370F8&wm_dtype=2014813&page_index=0&latitude=40814457&filter_type=0&'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.2.0'}
    response, content = http.request(url, method='POST', body=body, headers=headers)
    content = content.decode('utf-8')
