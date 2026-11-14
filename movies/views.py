from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from movies.serializers import UserSerializer,MovieSerializer,ReviewSerializer
from django.contrib.auth.models import User
from rest_framework import permissions,authentication
from movies.models import MovieDb,ReviewDb 
from rest_framework import serializers

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

class MovieRetriveUpdateDeleteView(APIView):
    permission_classes =[permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    def get(self,request,pk):
        movie = get_object_or_404(MovieDb,id=pk)
        if movie.created_by == request.user:
            serializers_instances = MovieSerializer(movie)
            return Response(data=serializers_instances.data)
        return Response(data={"Message":"You hvae No Access"})
    def put(self,request,pk):
        movie = get_object_or_404(MovieDb,id=pk)
        if movie.created_by != request.user:
            return serializers.ValidationError("Access Denied")
        form_data = request.data
        serializers_instances = MovieSerializer(movie,data=form_data)
        if serializers_instances.is_valid():
            serializers_instances.save()
            return Response(data={
                "Message":"Movie Details Updated"
            })
        return Response(data=serializers_instances.errors)

    def delete(self,request,pk):
        movie = get_object_or_404(MovieDb,id=pk)
        if movie.created_by == request.user:
            movie.delete()
            return Response(data={"Message":"Movie Deleted Succesfully"},status=200)
        return Response(status=403)

class ReviewcreateListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    def get(self,request):
        movie = ReviewDb.objects.all()
        serializer_instances = ReviewSerializer(movie,many=True)
        return Response(data=serializer_instances.data)

    def post(self,request):
        movie_id = request.data.get('movie_id')
        movie = get_object_or_404(MovieDb,id=movie_id)
        serializer_instances = ReviewSerializer(data=request.data)
        if serializer_instances.is_valid():
            serializer_instances.save(
                user = request.user,
                movie=movie
            )
            return Response({
                    "Message": "Review Added Successfully",
                    "data": serializer_instances.data
                })
        return Response(data=serializer_instances.errors)
