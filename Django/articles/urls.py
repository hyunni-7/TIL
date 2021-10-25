from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 기초 연습
    # path('html/', views.respond_with_html),
    # path('json-1/', views.respond_with_json_1),
    # path('json-2/', views.respond_with_json_2),
    # path('json-3/', views.respond_with_json_3),

    # urls for API
    path('articles/', views.respond_with_articles),
    path('articles/<int:art_pk>/', views.respond_with_article),
]
