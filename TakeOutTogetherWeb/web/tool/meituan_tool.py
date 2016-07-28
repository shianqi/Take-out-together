import time
import httplib2
from math import log10

#  Note: the alphabet in geohash differs from the common base32
#  alphabet described in IETF's RFC 4648
#  (http://tools.ietf.org/html/rfc4648)
__base32 = '0123456789bcdefghjkmnpqrstuvwxyz'
__decodemap = { }

def post(lat, lng, index = 0):
    http = httplib2.Http()
    url = 'http://i.waimai.meituan.com/home?lat={lat}&lng={lng}'
    url = url.replace('{lat}', str(lat))
    uro = url.replace('{lng}', str(lng))
    body = 'page_index={index}&apage=1'
    body = body.replace('{index}', str(index))
    cookie = 'uuid=..0.0.0; oc=--; abt=1454175307.0%7CACE; iuuid=; ioc=--; ci=191; webp=1; poiid=1218741; _ga=GA1.2.1578715842.1469542721; w_addr=; w_visitid=; wx_channel_id=0; terminal=i; w_utmz="utm_campaign=(direct)&utm_source=0&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_uuid=9ee53e87-af66-443a-a3ff-5c504b9c587a; utm_source=0; w_cid=; w_cpy_cn=""; w_cpy=; w_geoid={geohash}; w_latlng={lat},{lng}; JSESSIONID=; __mta=....21'
    cookie = cookie.replace('{lat}', str(lat * 1000000))
    cookie = cookie.replace('{lng}', str(lng * 1000000))
    cookie = cookie.replace('{geohash}', encodeGeo(lat, lng))
    # print(cookie)
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.2.0', 'Cookie' : cookie}
    response, content = http.request(url, method='POST', body=body, headers=headers)
    # content = content.decode('utf-8')
    content = eval(content)
    data = content.get('data')
    stepLength = (len(data) & 7) + 1
    result = ''
    for i in range(len(data)):
        #print(chr(ord(data[i])-stepLength))
        result += str(chr(ord(data[i])-stepLength))
    # print(decode(content.get('data')))
    # print(len(data))
    return result

def encodeGeo(latitude, longitude, precision=12):
    """
    Encode a position given in float arguments latitude, longitude to
    a geohash which will have the character count precision.
    """
    lat_interval, lon_interval = (-90.0, 90.0), (-180.0, 180.0)
    geohash = []
    bits = [ 16, 8, 4, 2, 1 ]
    bit = 0
    ch = 0
    even = True
    while len(geohash) < precision:
        if even:
            mid = (lon_interval[0] + lon_interval[1]) / 2
            if longitude > mid:
                ch |= bits[bit]
                lon_interval = (mid, lon_interval[1])
            else:
                lon_interval = (lon_interval[0], mid)
        else:
            mid = (lat_interval[0] + lat_interval[1]) / 2
            if latitude > mid:
                ch |= bits[bit]
                lat_interval = (mid, lat_interval[1])
            else:
                lat_interval = (lat_interval[0], mid)
        even = not even
        if bit < 4:
            bit += 1
        else:
            geohash += __base32[ch]
            bit = 0
            ch = 0
    return ''.join(geohash)