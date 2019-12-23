from django.urls import path
from .views import query_article,add_article,modify_article,delete_article,test_api

urlpatterns = [
    path('query_article/', query_article, name='query_article'),
    path('add_article/', add_article, name='add_article'),
    path('modify_article/<int:article_id>', modify_article, name='modify_article'),
    path('delete_article/<int:article_id>', delete_article, name='delete_article'),
    path('test_api/', test_api, name='test_api')
]