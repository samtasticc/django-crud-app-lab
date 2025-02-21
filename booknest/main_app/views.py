from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Author
from .forms import BookForm

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('author-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def author_index(request):
    authors = Author.objects.filter(user=request.user)
    return render(request, 'authors/index.html', {'authors': authors})

@login_required
def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    book_form = BookForm()
    return render(request, 'authors/detail.html', {'author': author, 'book_form': book_form})

@login_required
def add_book(request, author_id):
    form = BookForm(request.POST)
    if form.is_valid():
        new_book = form.save(commit=False)
        new_book.author_id = author_id
        new_book.save()
    return redirect('author-detail', author_id=author_id)

class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name', 'age', 'genre', 'nationality', 'bio']
    success_url = '/authors/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['name', 'age', 'genre', 'nationality', 'bio']

class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = '/authors/'






