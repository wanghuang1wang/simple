from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from apps.article.models import Article
from .models import Comment
import datetime,json
from django.views.generic import View
class CommentView(View):
    def get(self,request):
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        aricle_id = request.GET['title']
        title_id = Article.objects.filter(id=int(aricle_id))[0]
        print(title_id)
        desc = request.GET['key']
        test = Comment()
        print(desc)
        test.ariticle = str(title_id.title)
        test.comment_desc = desc
        test.comment_time = nowTime
        test.save()
        return HttpResponse(json.dumps("评论成功"))

#评论
# def CommentLike(request):
#     nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     aricle_id = request.GET['title']
#     title_id = Article.objects.filter(id=int(aricle_id))[0]
#     print(title_id)
#     desc = request.GET['key']
#     test = Comment()
#     print(desc)
#     test.ariticle = str(title_id.title)
#     test.comment_desc = desc
#     test.comment_time = nowTime
#     test.save()
#     return HttpResponse(json.dumps("评论成功"))