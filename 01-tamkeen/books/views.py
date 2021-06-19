from django.http import request
from django.shortcuts import render
from .models import Authors, Book, Categories, Publishers, Stores
from django.shortcuts import get_object_or_404
# from common.decorators import ajax_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse



# Create your views here.


def ShowBooks(request):
    context = {
        "books": Book.objects.filter(available=True, showinSlideShow=True)[:12]
    }

    return render(request, 'books/listbooks.html', context)
    # return render(request,'base.html',context)


def Detail(request, pk):
    context = {
        "book": get_object_or_404(Book, pk=pk),
        "categories": Categories.objects.all().filter(publish=True),
        # "authors": Authors.objects.all().filter(publish=True),
        "publishers": Publishers.objects.all().filter(publish=True),
    }

    return render(request, 'books/single.html', context)
    # return render(request, 'books/detail.html', context)


# stores = models.ManyToManyField( Stores, verbose_name=("المتجر"), related_name="store_book",)
def book_list(request):
    books = Book.objects.all().filter(publish=True)
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

    context = {
        "categories": Categories.objects.all().filter(publish=True),
        # "authors": Authors.objects.all().filter(publish=True),
        "publishers": Publishers.objects.all().filter(publish=True),
        "books": books,
    }

    return render(request, 'books/books_list.html', context)


def books_Publisher(request, pk):
    books = Book.objects.all()
    section = get_object_or_404(Publishers, pk=pk)
    books = books.filter(Publishers=section)
    section = section.name_publisher

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

    context = {
        "categories": Categories.objects.all().filter(publish=True),
        # "authors": Authors.objects.all().filter(publish=True),
        "publishers": Publishers.objects.all().filter(publish=True),
        "books": books,
        'section': section,
    }

    return render(request, 'books/books_list.html', context)


def books_category(request, pk):
    books = Book.objects.all()
    section = get_object_or_404(Categories, pk=pk)
    books = books.filter(Categories=section)
    section = section.name_category

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

    context = {
        "categories": Categories.objects.all().filter(publish=True),
        # "authors": Authors.objects.all().filter(publish=True),
        "publishers": Publishers.objects.all().filter(publish=True),
        "books": books,
        'section': section,
    }

    return render(request, 'books/books_list.html', context)


def books_author(request, pk):
    books = Book.objects.all()
    section = get_object_or_404(Authors, pk=pk)
    books = books.filter(auther=section)
    section = section.name_author

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

    context = {
        "categories": Categories.objects.all().filter(publish=True),
        # "authors": Authors.objects.all().filter(publish=True),
        "publishers": Publishers.objects.all().filter(publish=True),
        "news_pro": Book.objects.filter(publish=True).order_by('-id')[:5],
        "books": books,
        'section': section,
    }

    return render(request, 'books/books_list.html', context)


def Home(request):
    context = {
        "books": Book.objects.filter(available=True, showinSlideShow=True)[:12],
        "news_pro": Book.objects.filter(available=True).order_by('-id')[:4],
        "top_sell": Book.objects.filter(available=True).order_by('-id')[:43],
        "top_ranks": Book.objects.filter(available=True).order_by('-price')[:43],
        "categories": Categories.objects.all().filter(publish=True),
        "authors": Authors.objects.all().filter(publish=True),
        "publishers": Publishers.objects.all().filter(publish=True),
    }
    return render(request, 'books/Home.html', context)
