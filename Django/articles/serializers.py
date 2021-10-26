from rest_framework import serializers
from .models import Article

class ArticleSerializerAll(serializers.ModelSerializer):

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('id', 'title',)


class ArticleSerializerOne(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'