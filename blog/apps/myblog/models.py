from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# 用户模型.   后期处理 多用户系统  不能登陆后台
class UserProfile(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', max_length=200, blank=True, null=True, verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')

    class Meta:
        db_table = 'UserProfile'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.username


