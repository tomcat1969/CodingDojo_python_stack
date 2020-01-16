from django.shortcuts import render,redirect
from .models import Book,Author
def index(request):
    context={
        "all_the_books":Book.objects.all(),
        "all_the_authors":Author.objects.all()
    }
    return render(request,"index.html",context)
def showBook(request,book_id):
    mybook = Book.objects.get(id=book_id)
    context={
        "mybook":mybook,
        "all_the_authors":Author.objects.all()
    }
    return render(request,"book.html",context)
def addAuthor(request):
    author_id = request.POST['author_id']
    book_id = request.POST['book_id']
    myAuthor = Author.objects.get(id=author_id)
    mybook = Book.objects.get(id=book_id)
    mybook.authors.add(myAuthor)
    return redirect(f'books/{book_id}')
