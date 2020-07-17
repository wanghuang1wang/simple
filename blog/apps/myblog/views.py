# _*_ encoding:utf-8 _*_
from pure_pagination import Paginator, PageNotAnInteger
from django.shortcuts import render

from django.db.models.aggregates import Count

from django.conf import settings
from django.views.generic import View
from apps.article.models import Article,Category,PhotoAlbum,FriendsChain
# Create your views here.


def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME,
            'SITE_DESC': settings.SITE_DESC,}



# 博客首页
class Index(View):
    def get(self,request):
        article = Article.objects.all().order_by("-date_publish")
        # cate = Category.objects.all()

        #我的相册推荐首页
        photo_tj = PhotoAlbum.objects.filter(is_recommend=True)

        #文章分类
        cate = Category.objects.annotate(num_posts=Count('article'))
        #站长推荐
        recommend_articles = Article.objects.filter(is_recommend=True)

        # 友链
        frechain = FriendsChain.objects.all()
        # paginator = Paginator(article,3)  #分页对象  每页显示几条数据
        # # paginator.count   #总条目数
        # # paginator.num_pages  #可以分页的数量
        # # paginator.page_range    #页面的范围
        #
        # #方法  get_page()
        # page = request.Get.get('page',1)  #取得page值，如果没有默认为1
        # page = paginator.get_page(page)
        # # page.has_next()  #有没有下一页
        # # page.has_previous()  #判断是否存在下一页
        # # page.next_page_number()  #获取下一页的页码数
        # # page.previous_page_number()#获取前一页的页码数
        #
        # #属性
        # #object_list  当前页额所有对象
        # #number  当前的页码数
        # #paginator  分页器对象

        # 进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(article, 10 )
        pages = p.page(page)

        return render(request, 'index.html', {
            # "article":article,
            'article':pages,
            'cate':cate,
            'recommend_articles':recommend_articles,
            'photo_tj':photo_tj,
            'frechain':frechain
        })