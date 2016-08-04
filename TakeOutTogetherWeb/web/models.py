from django.db import models

# Create your models here.
class Img_mapping(models.Model):
    native_url = models.CharField(max_length=250)
    qiniu_url = models.CharField(max_length=250)

    def __str__(self):
        return 'native_url=' + self.native_url + ' qiniu_url=' + self.qiniu_url

class Message(models.Model):
    msg = models.CharField(max_length=250)

    def __str__(self):
        return 'id=' + str(self.id) + '    msg=' + self.msg

class Update(models.Model):
    version = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    file_size = models.IntegerField(default=0)

    def __str__(self):
        return 'version:' + self.version + '    url:' + self.url  + '    size:' + str(self.file_size)


class Admin(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)


