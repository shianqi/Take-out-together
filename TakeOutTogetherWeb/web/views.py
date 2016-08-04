from django.views.decorators.csrf import csrf_exempt

from web.tool import json_tool
from django.http import HttpResponse

from django.shortcuts import render_to_response

from web.models import Admin
from django.template import RequestContext
from web.models import Message,Update
from web.tool.bean import MessageModel,UpdateModel
from web.crawler.crawler import get_shop_list

# Create your views here.
def index(request):
    # lat lng 为经纬度
    lng = request.GET.get('lng')
    lat = request.GET.get('lat')
    # 经纬度
    source = request.GET.get('source')
    # 页数
    page = request.GET.get('page')

    if page is None:
        page = 0
    # page = int(page)
    # if page == 0:
    #     list_str = json_tool.class_to_json(get_shop_list(lat, lng, source))
    #     request.session['list'] = list_str
    # else:
    #     list_str = request.session['list']
    #     print('len:' + str(len(eval(list_str))))
    #     if len(eval(list_str)) == 0:
    #         list_str = json_tool.class_to_json(get_shop_list(lat, lng, source))
    #         request.session['list'] = list_str
    # c_list = []
    # if page == 0:
    #     c_list = eval(list_str)[0:10]
    # else:
    #     c_list = eval(list_str)[2+8*page:10+8*page]
    # # list = get_shop_list(lat,lng,source)

    json_str = json_tool.class_to_json(get_shop_list(lat,lng,source))
    response = HttpResponse(json_str)
    response["Access-Control-Allow-Origin"] = "*"
    return response

# 消息
def message(request):
    messages = Message.objects.all()
    msg_model = MessageModel()
    if len(messages) == 0:
        msg_model.flag = 0
        msg_model.msg = ''
    else:
        msg_model.flag = 1
        msg_model.msg = messages[len(messages)-1].msg

    json_str = json_tool.class_to_json(msg_model)
    response = HttpResponse(json_str,content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response


# 升级
def update(request):
    now_version = request.GET.get('ver')
    updates = Update.objects.all()
    update_model = UpdateModel()
    if len(updates)==0:
        update_model.flag = 0
        update_model.url = ''
        update_model.ver = 0
        update_model.size = 0
    else:
        least_version = updates[len(updates)-1].version
        if now_version is not None and least_version == now_version:
            update_model.flag = 0
            update_model.url = ''
            update_model.ver = now_version
            update_model.size = 0
        else:
            update_model.flag = 1
            update_model.url = updates[len(updates)-1].url
            update_model.ver = updates[len(updates)-1].version
            update_model.size = updates[len(updates)-1].file_size
    json_str = json_tool.class_to_json(update_model)
    response = HttpResponse(json_str, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response


# 用户登录界面，未完成
def web_login_html(request):
    return render_to_response('web_login.html')


# 判断用户的的逻辑，未完成
@csrf_exempt
def web_login_py(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username is None or password is None:
        return  render_to_response('web_login.html')

    admins = Admin.objects.filter(username__exact=username,password__exact=password)
    if len(admins) == 0:
        return render_to_response('web_login.html',{'login_msg': '用户名或者密码不正确'})
    else:
        request.session['username'] = username
        request.session['user_id'] = admins[0].id
        return render_to_response('web_admin.html',{'username':username},context_instance=RequestContext(request))