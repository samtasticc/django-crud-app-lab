from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('authors/', views.author_index, name='author-index'),
    path('authors/<int:author_id>/', views.author_detail, name='author-detail'),
    path('authors/create', views.AuthorCreate.as_view(), name='author-create'),
]