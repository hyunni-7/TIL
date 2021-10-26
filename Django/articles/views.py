from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializerOne, ArticleSerializerAll

# Create your views here.
@api_view(['GET', 'POST'])
def respond_with_articles(request):
    # GET --> 전체 게시글 조회
    if request.method == 'GET':
        articles = get_list_or_404(Article)  # 데이터 조회
        serializer = ArticleSerializerAll(articles, many=True)  # serializing on "조회 데이터"
        return Response(serializer.data)  # 데이터 반환

    # POST --> 게시글 생성
    elif request.method == 'POST':
        serializer = ArticleSerializerOne(data=request.data)  # serializing on "request로 받은 데이터"
        if serializer.is_valid(raise_exception=True):  # 유효성 검사, 실패하면 기본적으로 status code 400 반환
            serializer.save()  # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 데이터 반환


@api_view(['GET', 'DELETE', 'PUT'])
def respond_with_article(request, art_pk):
    article = get_object_or_404(Article, pk=art_pk)  # 데이터 조회

    # GET --> 특정 게시글 조회
    if request.method == 'GET':
        serializer = ArticleSerializerOne(article)  # serializing on "조회 데이터"
        return Response(serializer.data)  # 데이터 반환

    # DELETE --> 특정 게시글 삭제
    elif request.method == 'DELETE':
        article.delete()  # 삭제
        message = {
            'delete!': f'{art_pk}번째 게시글이 삭제되었습니다.',  # 삭제 되었다는 것을 나타내는 임시 데이터(일종의 메시지)
        }
        return Response(message, status=status.HTTP_204_NO_CONTENT)  # 데이터 반환

    # PUT --> 특정 게시글 수정
    elif request.method == 'PUT':
        # serializing on "조회 데이터" regarding "request로 받은 데이터"
        serializer = ArticleSerializerOne(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):  # 유효성 검사, 실패하면 기본적으로 status code 400 반환
            serializer.save()  # 저장
            return Response(serializer.data)  # 데이터 반환
