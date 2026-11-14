from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

class MovieDb(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

class ReviewDb(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(MovieDb, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints =[models.UniqueConstraint(fields=['user','movie'],name='unique_user_movie')]

    def __str__(self):
        return self.movie.title