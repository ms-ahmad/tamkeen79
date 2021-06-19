
from django.shortcuts import redirect, render
from .models import Factor ,Factor_Detailes
from django.http import request
from books.models import Book
from django.urls import reverse
from django.views.generic.base import RedirectView
from django.db.models import F

# Create your views here.


def Add_to_cart(request, pk):
    tstInt =2222222
    bookadd = Book.objects.get(pk=pk)
    obj,openfactor = Factor.objects.get_or_create(id_user=request.user, is_send=False)
    tstInt = obj.id

    Factor_Ditl = Factor_Detailes.objects.filter(
        book_id=pk, factor_id__id=obj.id)
    # Factor_Ditl = Factor_Ditl1.get(factor_id__id=obj.id)
    if Factor_Ditl:
        pricebook = bookadd.price

        Factor_Ditl0 = Factor_Ditl.filter(factor_id__id=obj.id).update(book_count=F('book_count') + 1,)
        Factor_Ditl2 = Factor_Ditl.filter(factor_id__id=obj.id).update(detail_price=F('book_count')*bookadd.price)
        # Factor_Ditl.update(book_count=newcount)
        tstInt="yes"
    else:
        Factor_De = Factor_Detailes(factor_id=obj,)
        Factor_De.detail_price = Factor_De.book_count * bookadd.price

        tstInt=Factor_De.book_count
        Factor_De.save()
        Factor_De.book_id.add(pk)

      



    
    return render(request, 'factors.html', {"openfactor": openfactor, "a": tstInt, })
