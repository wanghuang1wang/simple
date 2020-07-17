from django.core.paginator import PageNotAnInteger,Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models.aggregates import Count

from django.views.generic import View
import markdown
from .models import Article,Category,ArticleTag,PhotoAlbum
#点赞
import json
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from apps.comment.models import Comment

# Create your views here.



#文章详情页
class ArticleView(View):
    def get(self,request,article_id):
        # article_xg = Article.objects.get(id=int(article_id))
        article_info = get_object_or_404(Article, pk=article_id)
        article_info.click_count +=1
        article_info.save()
        article_info.content = markdown.markdown(article_info.content,extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',  # 语法高亮拓展
            'markdown.extensions.toc'  # 自动生成目录
        ])
        catetory = article_info.category
        #相关文章查询
        xg = Article.objects.filter(category=catetory)
        ar_id = article_info.id #获取当前文章 id
        #下一篇
        next_ar = Article.objects.filter(id__gt=ar_id).order_by('id').first()
        #上一篇
        pro_ar = Article.objects.filter(id__lt=ar_id).order_by('-id').first()
        #文章详情左栏
        # 文章分类
        cate_fen = Category.objects.annotate(num_posts=Count('article'))
        #点击量排行
        click_articles = Article.objects.all().order_by('-click_count')[:6]
        # 站长推荐
        recommend_articles = Article.objects.filter(is_recommend=True)[:6]
        #标签云
        tag_all = ArticleTag.objects.all()
        # 评论
        com_title= article_info.title

        comment = Comment.objects.filter(ariticle=com_title)

        return render(request, 'info.html', {
            'article_info':article_info,
            'next_ar':next_ar,
            'pro_ar':pro_ar,
            'catetory':catetory,
            'list_about':xg,
            'info_le_fen':cate_fen,
            'info_le_cli':click_articles,
            'info_le_rec':recommend_articles,
            'info_le_tag':tag_all,
            'comment':comment,
        })






#文章随笔

class ArticlesuibiView(View):
    def get(self,request):

        getoutarticle = Article.objects.all()

        # 文章分类
        cate_fen = Category.objects.annotate(num_posts=Count('article'))


        getout_article = getoutarticle.filter(category__name='随笔')
        print(getout_article)
        #点击量排行
        click_articles = Article.objects.all().order_by('-click_count')[:6]

        # 站长推荐
        recommend_articles = Article.objects.filter(is_recommend=True)[:6]

        #标签云
        tag_all = ArticleTag.objects.all()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(getout_article, 10)
        suibi_pages = p.page(page)


        return render(request, 'list.html', {
            # 'getout_article':getout_article,
            'suibi_pages':suibi_pages,
            'cate_fen':cate_fen,
            'recommend_articles':recommend_articles,
            'click_articles':click_articles,
            'tag_all':tag_all,
        })



#文章搜索：
class SearchView(View):
    def get(self,request):
        keyboard = request.GET.get('keyboard')

        all_articles = Article.objects.all()

        if keyboard:
            articles = all_articles.filter(Q(title__contains=keyboard) |Q(user__username__icontains=keyboard) \
                                           | Q(category__name__icontains=keyboard) | Q(content__in=keyboard))  #看显示的名称是否包含自己所需的标签
        else:
            return HttpResponse('未找到')

        return render(request, 'search.html', {
            'search_articles': articles,

        })




class CategoryView(View):

    def get(self,request,pk):
        cate = get_object_or_404(Category,pk=pk)

        if cate:
            category_list = Article.objects.filter(category= cate)
            print(category_list)
            return render(request, 'fenlei.html', {'category':category_list})
        else:
            return HttpResponse('敬请期待')   #没弄好



class PhotoView(View):
    def get(self,request):
        photo = PhotoAlbum.objects.all()
        return render(request, 'share.html', {
            'photo':photo,
        })



#点赞

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')

        return json.JSONEncoder.default(self, obj)




def GiveLike(request,):
    like_id =request.GET['key']
    like_c = Article.objects.filter(id = like_id)[0]
    like_c.like_click += 1
    like_c.save()

    return HttpResponse(json.dumps({"id":"点赞成功"}))