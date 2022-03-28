from urllib import request
from django.db import models


# Create your models here.
class Movie(models.Model):


    class TYPE:
        MOVIE = 'MOVIE'
        TRAILER = 'TRAILER'
        SHOW = 'SHOW'
        SERIES = 'SERIES'
    
    
        CHOICE = (
            (MOVIE, MOVIE),
            (TRAILER, TRAILER),
            (SHOW, SHOW),
            (SERIES, SERIES)
        )


    title = models.CharField(max_length=150)
    released_year = models.IntegerField(null=True)
    language = models.CharField(max_length=50, null=True)
    duration = models.CharField(max_length=50, null=True)
    views_count = models.IntegerField(default=0)
    sourse_link = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=7, choices=TYPE.CHOICE, default=TYPE.MOVIE)
    banner = models.ImageField(upload_to='Banners', null=True)
    slug = models.SlugField(max_length=250)
    category_id = models.IntegerField(null=True, blank=True)


    def __str__(self) -> str:
        return self.title




class MovieCreate(Movie):
    request