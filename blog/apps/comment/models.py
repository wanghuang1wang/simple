from django.db import models
from apps.article.models import Article

# Create your models here.

class Comment(models.Model):
    """评论者、时间，文章、评论内容"""
    comment_desc = models.CharField(max_length=100, verbose_name='评论内容')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    ariticle = models.CharField(verbose_name='评论文章',max_length=30)


    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name