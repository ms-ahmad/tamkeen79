from django.http import request
from django.shortcuts import render
from .models import Book, Stores
from django.shortcuts import get_object_or_404
# from common.decorators import ajax_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

# Create your views here.


def Home(request):
    context = {
        "books": Book.objects.filter(available=True, showinSlideShow=True)[:12] ,
        "news_pro": Book.objects.filter(available=True).order_by('-id')[:4] ,
        "top_sell": Book.objects.filter(available=True).order_by('-id')[:43],
        "top_ranks": Book.objects.filter(available=True).order_by('-price')[:43],
    }
    return render(request, 'books/Home.html', context)



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


# stores = models.ManyToManyField( Stores, verbose_name=("المتجر"), related_name="store_book",)
def book_list(request):   
    books = Book.objects.all()
    # books = books.filter(stores__id=2)
    
    paginator = Paginator(books, 3)
    page = request.GET.get("page")
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return HttpResponse('')
        books = paginator.page(paginator.num_pages)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'books/books_list_ajax.html', {"books": books})

    return render(request, 'books/books_list.html', {"books": books,})


def book_store(request, pk):
    books = Book.objects.all()
    books = books.filter(stores__id=pk)
    section = get_object_or_404(Stores,pk=pk)
    section = section.name_store
    
    paginator = Paginator(books, 3)
    page = request.GET.get("page")
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return HttpResponse('')
        books = paginator.page(paginator.num_pages)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'books/books_list_ajax.html', {"books": books, 'section': "store"})

    return render(request, 'books/books_list.html', {"books": books, 'section': section})
