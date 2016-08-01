from django.test import TestCase
from web.crawler import  meituan_crawler,meituan_web_crawler
from httplib2 import Http
from web.tool.qiniu.utils import urlsafe_base64_encode
from web.tool.qiniu.auth import Auth
from web.tool.img_tool import img_shrink

img_shrink('http://img.waimai.bdimg.com/pb/c644dab340b74e327aa7625c31c6bc5521','BD123')

