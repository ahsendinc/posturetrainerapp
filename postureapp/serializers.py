from django.contrib.auth.models import User,Group
from rest_framework import serializers
from postureapp.models import Document, Recommendation, PickleObject


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ('docfile', 'pub_date')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class RecommendationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recommendation
        fields = ('repstatus', 'pub_date')

class PickleObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PickleObject
        fields = ('args', 'name')
