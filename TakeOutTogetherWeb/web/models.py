from django.db import models

# Create your models here.
class Img_mapping(models.Model):
    native_url = models.CharField(max_length=250)
    qiniu_url = models.CharField(max_length=250)