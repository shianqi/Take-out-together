from django.contrib import admin
from .models import Message,Img_mapping,Update
# Register your models here.

admin.site.register(Message)
admin.site.register(Img_mapping)
admin.site.register(Update)