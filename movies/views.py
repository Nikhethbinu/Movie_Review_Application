from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from movies.serializers import UserSerializer,MovieSerializer
from django.contrib.auth.models import User
from rest_framework import permissions,authentication
from movies.models import MovieDb

class SignUpView(APIView):
    def post(self,request):
        form_data =request.data
        serializers_instances = UserSerializer(data=form_data)
        if serializers_instances.is_valid():
            serializers_instances.save()
            return Response({
                "Message":"Signed Up Successfully"
            })
        return Response(data=serializers_instances.data)

class UserListView(APIView):  
    def get(self,request):
        qs = User.objects.all()
        serializers_instances = UserSerializer(qs,many=True)
        return Response(data=serializers_instances.data)

class MovieListCreateView(APIView):
    permission_classes =[permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    def post(self,request):
        form_data = request.data
        serializers_instances = MovieSerializer(data=form_data)
        if serializers_instances.is_valid():
            serializers_instances.save(created_by=request.user)
            return Response(data={
                "Message":"Movie Added Successfully"
            },status=201)
        return Response(data=serializers_instances.errors,status=400)

    def get(self,request):
        qs = MovieDb.objects.all()
        serializers_instances = MovieSerializer(qs,many=True)
        return Response(data=serializers_instances.data)