from django.db import models

# Create your models here.
class CCharField(models.Field):

    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(CCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        return 'char(%s)' %(self.max_length)

class Users(models.Model):

    username = models.CharField(max_length=20)
    pwd = CCharField(max_length=20)



















