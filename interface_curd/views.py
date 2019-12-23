from django.http import HttpResponse,JsonResponse
from .models import Article
import json
# Create your views here.
def query_article(request):
    if request.method == 'GET':
        articles = {}
        query_articles = Article.objects.all()
        print('query_articles:',query_articles)
        for title in query_articles:
            articles[title.title] = title.status
        return JsonResponse({"status": "BS.200", "all_titles": articles, "msg": "query articles success."})
        print("request.body", request.body)
    else:
        return HttpResponse("方法错误")

def add_article(request):
    auth_res = user_auth(request)
    if auth_res == "auth_fail":
        return JsonResponse({"status": "BS.401", "msg": "user auth failed."})
    else:
        if request.method == 'POST':
            # b''
            print('request.body: ', request.body)
            print('request.body: ', type(request.body))
            req_dict = json.loads(request.body)
            print('req_json: ', req_dict)
            print('req_json: ', type(req_dict))
            key_flag = req_dict.get('title') and req_dict.get('content') and len(req_dict) == 2
            print('key_flag: ', key_flag)
            # 判断请求体是否正确
            if key_flag:
                title = req_dict['title']
                content = req_dict['content']
                # title返回的是一个list
                title_exist = Article.objects.filter(title=title)
                # 判断是否存在同名的title
                if len(title_exist) != 0:
                    return JsonResponse({"status": "BS.400", "msg": "title already exist, fail to publish."})
                """
                插入数据
                """
                add_art = Article(title=title, content=content, status='alive')
                add_art.save()
                return HttpResponse(add_art)
                return JsonResponse({"status": "BS.200", "msg": "add article success."})
            else:
                return JsonResponse({"status": "BS.400", "message": "please check param."})
        else:
            return HttpResponse("方法错误，你应该使用POST请求方式")

def modify_article(request,article_id):
    auth_res = user_auth(request)
    if auth_res == "auth_fail":
        return JsonResponse({"status": "BS.401", "msg": "user auth failed."})
    else:
        if request.method == 'POST':
            modify_req = json.loads(request.body)
            try:
                article = Article.objects.get(id=article_id)
                print("article", article)
                key_flag = modify_req.get('title') and modify_req.get('content') and len(modify_req) == 2
                if key_flag:
                    title = modify_req['title']
                    content = modify_req['content']
                    title_exist = Article.objects.filter(title=title)
                    if len(title_exist) > 1:
                        return JsonResponse({"status": "BS.400", "msg": "title already exist."})

                    # 更新文章
                    old_article = Article.objects.get(id=article_id)
                    old_article.title = title
                    old_article.content = content
                    old_article.save()
                    return JsonResponse({"status": "BS.200", "msg": "modify article sucess."})
            except Article.DoesNotExist:
                return JsonResponse({"status": "BS.300", "msg": "article is not exists,fail to modify."})
        else:
            return HttpResponse("方法错误，你应该使用POST请求方式")

# 删除文章
def delete_article(request, article_id):
    auth_res = user_auth(request)
    if auth_res == "auth_fail":
        return JsonResponse({"status": "BS.401", "msg": "user auth failed."})
    else:
        if request.method == 'DELETE':
            try:
                article = Article.objects.get(id=article_id)
                article_id = article.id
                article.delete()
                return JsonResponse({"status": "BS.200", "msg": "delete article success."})
            except Article.DoesNotExist:
                return JsonResponse({"status": "BS.300", "msg": "article is not exists,fail to delete."})
        else:
            return HttpResponse("方法错误，你应该使用DELETE请求方式")

def test_api(request):
    data = {'name', 'test_name'}
    if request.method == 'POST':
        print('request.POST', request.POST)
        # return JsonResponse(data)
    else:
        return HttpResponse("方法错误")

# 用户认证
# 四个简单的接口已经可以运行了，但是在发请求之前没有进行鉴权，毫无安全性可言。下面来实现简单的认证机制。需要用到内建模块hashlib，hashlib提供了常见的摘要算法，如MD5，SHA1等。
def user_auth(request):
    token = request.META.get("HTTP_X_TOKEN", b'')
    print("token: ", token)
    if token:
        # 暂时写上 auth 接口返回的数据
        if token == '0a6db4e59c7fff2b2b94a297e2e5632e':
            return "auth_success"
        else:
            return "auth_fail"
    else:
        return "auth_fail"
