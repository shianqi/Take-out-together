from django.test import TestCase
from web.crawler import  meituan_crawler,meituan_web_crawler


lat = 111.695549
lng = 40.8205
meituan_web_crawler.get_shop_list(lng,lat)