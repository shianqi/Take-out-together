from django.test import TestCase

from web.crawler import meituan_web_crawler, meituan_crawler, baidu_crawler
from web.models import Message


class myTestCase(TestCase):
    def test1(self):
        print('123')
        message = Message()
        message.msg = 'test'
        message.save()
        print(message.id)
        message = Message()
        message.msg = '456'
        message.save()
        print(message.id)
        message = Message()
        message.msg = '789'
        message.save()
        print(message.id)

        msg_id = 2
        messages = Message.objects.filter(id__gt=msg_id)
        print(messages[0].msg)

    def test2(self):

        list = meituan_crawler.get_shop_list(40.81253, 111.690187)
        print(len(list))
        list = meituan_web_crawler.get_shop_list(40.81253, 111.690187)
        #lat = 40.81253 & lng = 111.690187 & source = meituanbaidueleme & page = 0
        
    def test3(self):
        list = baidu_crawler.get_shop_list(111.690187, 40.81253)
        print(len(list))



