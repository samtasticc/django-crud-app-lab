from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Author
from .forms import BookForm
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
    book_form = BookForm()
    return render(request, 'authors/detail.html', {'author': author, 'book_form': book_form})

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    success_url = '/authors/'

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name', 'age', 'genre', 'nationality', 'bio']

class AuthorDelete(DeleteView):
    model = Author
    success_url = '/authors/'

def add_book(request, author_id):
    form = BookForm(request.POST)
    if form.is_valid():
        new_book = form.save(commit=False)
        new_book.author_id = author_id
        new_book.save()
    return redirect('author-detail', author_id=author_id)

