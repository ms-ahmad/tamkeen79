from django.http import request
from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404

# Create your views here.


def ShowBooks(request):
    context ={
        "books": Book.objects.filter(available=True, showinSlideShow=True)[:12]
    }

    return render(request,'books/listbooks.html',context)
    # return render(request,'base.html',context)


def Detail(request,pk):
    context ={
        "book": get_object_or_404(Book,pk=pk) 
    }

    return render(request, 'books/detail.html', context)
