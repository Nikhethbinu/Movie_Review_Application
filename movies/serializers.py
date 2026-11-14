from rest_framework import serializers
from django.contrib.auth.models import User
from movies.models import MovieDb,ReviewDb

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

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)
    title = serializers.CharField(source='movie.title',read_only=True)
    movie_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = ReviewDb
        fields = ["movie_id","username","title","rating","comment","created_at"]
        read_only_fields = ["created_at"]
