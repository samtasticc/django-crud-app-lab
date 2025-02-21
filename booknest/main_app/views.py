from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Author
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def author_index(request):
    authors = Author.objects.all()
    return render(request, 'authors/index.html', {'authors': authors})

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'authors/detail.html', {'author': author})

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    success_url = '/authors/'
