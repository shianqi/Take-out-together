from django.contrib import admin
from .models import Message, Img_mapping, Update, Access_log
# Register your models here.

admin.site.register(Message)
admin.site.register(Img_mapping)
admin.site.register(Update)
admin.site.register(Access_log)
