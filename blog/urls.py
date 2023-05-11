
from django.urls import path

from . import admin, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors', views.DirectorList.as_view()),
    path('api/v1/directors/<int:id>', views.DirectorDetail.as_view()),
    path('api/v1/movies', views.MovieList.as_view()),
    path('api/v1/movies/<int:id>', views.MovieDetail.as_view()),
    path('api/v1/revies', views.ReviewList.as_view()),
    path('api/v1/revies/<int:id>', views.ReviewDetail.as_view()),
    path('api/v1/movies/reviews/', views.MovieReviewList.as_view(), name='movie_review_list'),
]