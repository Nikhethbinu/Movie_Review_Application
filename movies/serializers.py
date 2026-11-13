from rest_framework import serializers
from django.contrib.auth.models import User
from movies.models import MovieDb

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","username","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

    def __str__(self):
        return self.username

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDb
        fields =["title","description","release_year","genre","created_at","created_by"]
        read_only_fields =["created_at","created_by"]
    