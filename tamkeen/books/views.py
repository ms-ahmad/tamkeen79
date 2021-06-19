
from star_ratings.models import Rating
import random
from django.http import request
from django.shortcuts import render
from .models import Authors, Book, Categories, Publishers, Stores 
from django.shortcuts import get_object_or_404
# from common.decorators import ajax_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Count, Sum
from slides.models import slides, Comming_soon, Quotes
from orders.models import OrderDetails, Order


# Create your views here.


def Home(request):
    rate_books = []
    top_order = []


    for b in Rating.objects.all().order_by('-average')[:6]:
        rate_books.append(Book.objects.get(pk=b.object_id))

            #/////////////////////////////////////////// الاكثر طلبا
    sum_qty_book_orderdetails = OrderDetails.objects.values('book__id').annotate(Sum('quantity'))

    list_sum_qty_book_orderdetails = list(sum_qty_book_orderdetails)
    def myFunc(e):
        return e['quantity__sum']

    list_sum_qty_book_orderdetails.sort(reverse=True, key=myFunc)
    
    print(list_sum_qty_book_orderdetails[:3])

    for b in list_sum_qty_book_orderdetails[:3]:
        top_order.append(Book.objects.get(pk=b['book__id']))
   
            #//////////////////////////////////////////// نهاية  الاكثر طلبا


    context = {
        "books": Book.objects.filter(available=True, showinSlideShow=True)[:12],
        "news_pro": Book.objects.filter(available=True).order_by('-id')[:4],
        # "top_order": Book.objects.filter(available=True).order_by('-id')[:43],
        "top_ranks": rate_books,
        "top_order": top_order,
        "categories": Categories.objects.all().filter(publish=True),
        "authors": Authors.objects.all().filter(publish=True),
        "publishers": Publishers.objects.all().filter(publish=True),
        "slides": slides.objects.all().filter(show=True).order_by('-id'),
        "comming_soon": Comming_soon.objects.all().filter(publish=True).order_by('-id'),
        "quotes": Quotes.objects.all().filter(pubish=True).order_by('-id'),
        # "pubs": Publishers.objects.annotate(num_books=Count('book'))
   

    }
    return render(request, 'books/Home.html', context)





def ShowBooks(request):
    context = {
        "books": Book.objects.filter(available=True, showinSlideShow=True)[:12]
    }

    return render(request, 'books/listbooks.html', context)
    # return render(request,'base.html',context)


def Detail(request, pk):
    count_random_book =5
    def count_random(list, conunt_random_book):
        if len(list) <= conunt_random_book:
            conunt_random_book = len(list)
        return conunt_random_book


    book = get_object_or_404(Book, pk=pk)
    books = Book.objects.all()
            # كتب من نفس الناشر
    for b in book.Publishers.all():
        book_from_publisher = books.all().filter(Publishers=b)

    book_from_publisher =list(book_from_publisher)
    book_from_publisher = random.sample(book_from_publisher, count_random(book_from_publisher, count_random_book))


            # كتب من نفس المؤلف
    for A in book.auther.all():
        book_from_author = books.all().filter(auther=A)
        
    book_from_author =list(book_from_author)
    book_from_author = random.sample(book_from_author, count_random(book_from_author, count_random_book))
    
            # كتب من نفس الفئة
    for A in book.Categories.all():
        book_from_Categories = books.all().filter(Categories=A)
        
    book_from_Categories =list(book_from_Categories)
    book_from_Categories = random.sample(book_from_Categories, count_random(book_from_Categories, count_random_book))
    

                #كتب عشوائية 
    random_book =list(books)
    random_book = random.sample(random_book, count_random(random_book, count_random_book))
    



    context = {
        "object": get_object_or_404(Book, pk=pk),
        "categories": Categories.objects.all().filter(publish=True),
        # "authors": Authors.objects.all().filter(publish=True),
        "publishers": Publishers.objects.all().filter(publish=True),
        "book_from_publisher": book_from_publisher,
        "book_from_author": book_from_author,     
        "book_from_Categories": book_from_Categories,     
        "random_book": random_book,     

    }

    return render(request, 'books/single.html', context)
    # return render(request, 'books/detail.html', context)


# stores = models.ManyToManyField( Stores, verbose_name=("المتجر"), related_name="store_book",)
def book_list(request):
    books = Book.objects.all().filter(publish=True)
    # books = books.filter(stores__id=2)
    random_book =list(books)
    random_book = random.sample(random_book, 7)


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
        "comming_soon": Comming_soon.objects.all().filter(publish=True).order_by('-id')[:2],
        "random_book": random_book,
    }

    return render(request, 'books/books_list.html', context)


def books_Publisher(request, pk):
    books = Book.objects.all()
    random_book =list(books)
    random_book = random.sample(random_book, 7)
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
        "comming_soon": Comming_soon.objects.all().filter(publish=True).order_by('-id')[:2],
        "random_book": random_book,
      
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


# title_book=&categ=%25&author=%25&publisher=%25

def search(request,cat_id,publisher_id,author_id,title_book):
    # id_cat=request.GET['categ']
    sectiontext="نتائج البحث عن: "
    books = Book.objects.all()

    if title_book!="&":
        books = books.filter(title_book__contains=title_book)
        sectiontext +=" '"+ title_book+"'"


    if cat_id>0:
        section = get_object_or_404(Categories, id=cat_id)
        books = books.filter(Categories=section)
        sectiontext +=" "+  section.name_category


    if publisher_id>0:
        section = get_object_or_404(Publishers, pk=publisher_id)
        books = books.filter(Publishers=section)      
        sectiontext +=" - "+  section.name_publisher

        
    if author_id>0:
        section = get_object_or_404(Authors, pk=author_id)
        books = books.filter(auther=section)          
        sectiontext +=" - "+  section.name_author

    sectiontext +=" - عدد النتائج : ("+ str(books.count())+")"

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
        'section': sectiontext,
    }

    return render(request, 'books/books_list.html', context)