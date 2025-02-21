from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('authors/', views.author_index, name='author-index'),
    path('authors/<int:author_id>/', views.author_detail, name='author-detail'),
    path('authors/create', views.AuthorCreate.as_view(), name='author-create'),
    path('authors/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    path('authors/<int:author_id>/add-book/', views.add_book, name='add-book'),
    path('accounts/signup/', views.signup, name='signup'),
]