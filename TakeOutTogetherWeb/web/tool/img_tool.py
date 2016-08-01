from httplib2 import Http
from web.tool.qiniu.utils import urlsafe_base64_encode
from web.tool.qiniu.auth import Auth
from web.models import Img_mapping
"""
一个实现图片缩小的函数
"""

def img_shrink(img_url,img_id):
    img_mappings = Img_mapping.objects.filter(native_url__exact=img_url)
    if(len(img_mappings) != 0):
        return img_mappings[0].qiniu_url
    else:

        http = Http()
        url = 'http://iovip.qbox.me'
        body = '/fetch/<EncodedURL>/to/<EncodedEntryURI>'
        content_type = 'application/x-www-form-urlencoded'

        encoded_url = urlsafe_base64_encode(img_url)
        entry = 'hupeng:waimai/' + img_id
        encoded_entry_url = urlsafe_base64_encode(entry)
        body = body.replace('<EncodedURL>', encoded_url, ).replace('<EncodedEntryURI>', encoded_entry_url)

        auth = Auth('fj70Xmr_c09YUx9Yq1cL1Gl-KqJhQ8Oe1jVuhlRU', 'n7OVMl6fn19VP9ms-5dqrzE3mwoB1VRYPsT-4CFz')
        authorization = auth.token_of_request(url=url + body, content_type=content_type)
        authorization = 'QBox ' + authorization
        response, content = http.request(url + body, 'POST', headers={'Host': 'iovip.qbox.me', 'Content-Type': content_type,
                                                                      'Authorization': authorization})
        qiniu_url = 'http://7xloq8.com1.z0.glb.clouddn.com/waimai/' + img_id + '?imageView2/0/w/96/h/96/format/png/interlace/0/'
        img_mappings = Img_mapping()
        img_mappings.native_url = img_url
        img_mappings.qiniu_url = qiniu_url
        img_mappings.save()
        return qiniu_url