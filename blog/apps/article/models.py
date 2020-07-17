from django.db import models
from mdeditor.fields import MDTextField   # 必须导入 --->markdown

#


# Create your models here.
from apps.myblog.models import UserProfile
from django.shortcuts import reverse

class ArticleTag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称',null=False, blank=False)

    class Meta:

        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



# 文章分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField('显示顺序(从小到大)',default=999)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name






# # 文章模型
class Article(models.Model):

    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=50, verbose_name='文章描述')
    content = MDTextField()    # 注意为MDTextField()
    image = models.ImageField(upload_to="article/%Y/%m/%d",default='',max_length=100,verbose_name='文章图片',null=True,blank=True)
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(to=UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类',on_delete=models.CASCADE)
    tag = models.ManyToManyField(ArticleTag, verbose_name='标签')
    like_click = models.IntegerField(default=0, verbose_name='点赞次数')


    class Meta:

        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

        # 自定义 get_absolute_url 方法

    def get_absolute_url(self):

        return reverse('article:article', kwargs={'article_id': self.pk})


#友链。。。。
class FriendsChain(models.Model):
    url = models.CharField(max_length=100, verbose_name='友链url')
    name = models.CharField(max_length=100, verbose_name='友链名称')

    class Meta:
        verbose_name = "友链"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



#相册
class PhotoAlbum(models.Model):
    title = models.CharField(max_length=50, verbose_name='图片标题')
    desc = models.CharField(max_length=50, verbose_name='图片描述')
    content = MDTextField()
    img = models.ImageField(upload_to="photo/%Y/%m/%d",default='',max_length=100,verbose_name='相册图片',null=True,blank=True)
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')


    class Meta:
        verbose_name = "相册"
        verbose_name_plural = verbose_name





