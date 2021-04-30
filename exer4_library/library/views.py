from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    data = {"authors" : authors,"books" : books}
    return render(request, "library/home.html", data)

def addAuthor(request):
    form = AuthorForm()

    if (request.method == "POST"):
        form = AuthorForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect("/")

    data = {"form": form}
    return render(request, "library/addAuthor.html", data)

def addBook(request):
    form = BookForm()
    
    if (request.method == "POST"):
        form = BookForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect("/")

    data = {"form": form}
    return render(request, "library/addBook.html", data)

def updateAuthor(request, pk):
    author = Author.objects.get(id=pk)
    form = AuthorForm(instance=author)

    if (request.method == "POST"):
        form = AuthorForm(request.POST, instance=author)
        if (form.is_valid()):
            form.save()
            return redirect("/")

    data = {"form":form}
    return render(request, "library/updateAuthor.html", data)

def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if (request.method == "POST"):
        form = BookForm(request.POST, instance=book)
        if (form.is_valid()):
            form.save()
            return redirect("/")

    data = {"form":form}
    return render(request, "library/updateBook.html", data)

def deleteAuthor(request, pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return redirect("/")

def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect("/")