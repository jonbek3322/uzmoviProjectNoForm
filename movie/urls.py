from django.urls import path
from movie.views import movie_detail, movies_list, movie_create, movie_edit


urlpatterns = [
    path('', movies_list),
    path('<int:movie_id>', movie_detail),
    path('<int:movie_id>/edit', movie_edit),
    path('create', movie_create)
]
