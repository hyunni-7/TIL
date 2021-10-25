from django.shortcuts import render, get_list_or_404

from django.http.response import HttpResponse, JsonResponse
from django.core import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
def respond_with_html(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/sample.html', context)


def respond_with_json_1(request):
    """
    * django 내장 모듈(JsonResponse)을 활용한 serialization
    * 직접 구조 잡아주기
    """

    # step 1. 반환할 데이터 조회 --> get_list_or_404
    articles = get_list_or_404(Article)
    
    # step 2. 구조 잡기
    articles_json = []  # 최종적으로 반환할 리스트
    for article in articles:
        # 각 데이터 로우에 대하여 구조를 잡아준 후 리스트에 담기
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    # step 3. 반환 with JsonResponse at django.http.response
    return JsonResponse(articles_json, safe=False)  # dict type 이외의 객체에 대하여 serializing 하려면 False로 설정


def respond_with_json_2(request):
    """
    * django 내장 모듈(HttpResponse)을 활용한 serialization
    * 모델 정보 활용
    """

    # step 1. 반환할 데이터 조회 --> get_list_or_404
    articles = get_list_or_404(Article)

    # step 2. serializing with serializers.serialize at django.core (모델 정보를 활용하므로 구조를 직접 잡아줄 필요 없음)
    articles_serialized = serializers.serialize('json', articles)

    # step 3. 반환 with HttpResponse at django.http.response
    return HttpResponse(articles_serialized, content_type='application/json')


#############################################   MAIN CODE   #############################################
@api_view(['GET'])  # "필수" 데코레이터로 http method를 검증(필터링)
def respond_with_json_3(request):
    """
    * django 3rd-party library(Django REST framework, DRF)을 활용한 serialization
    * app 내에 serializers.py 생성(모델 정보 활용)
    """

    # step 1. 반환할 데이터 조회 --> get_list_or_404
    articles = get_list_or_404(Article)

    # step 2. serializing with ArticleSerializer at serializers (모델 정보를 활용하므로 구조를 직접 잡아줄 필요 없음)
    serializer = ArticleSerializer(articles, many=True)  # 여러 데이터 로우에 대하여 serializing 한다면 True로 설정

    # step 3. 반환 with Response at rest_framework.response
    return Response(serializer.data)
