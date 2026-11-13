from django.db import models
from django.contrib.auth.models import User

class MovieDb(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)