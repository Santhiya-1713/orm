from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from .models import Book
from .forms import BookForm

# Create your views here.
class BookListView(ListView):
    model=Book
    template_name='book_list.html'
    context_object_name='books'
class BookDetailView(DetailView):
    model=Book
    template_name='bookstore/book_detail.html'
    context_object='book'
def add_books(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form=BookForm()
        return render(request,'bookstore/index.html',{'form':form})