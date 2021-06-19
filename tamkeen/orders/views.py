from django.conf import settings
from django.db.models import F
from django.shortcuts import render, redirect
from django.contrib import messages
from books.models import Book, Categories, Publishers
from .models import Order
from .models import OrderDetails
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail




# Create your views here.


@login_required
def add_to_cart(request):
    
    if 'book_id' in request.GET and 'quantity' in request.GET and request.user.is_authenticated and not request.user.is_anonymous:

        book_id = request.GET['book_id']
        qty = request.GET['quantity']

        if not Book.objects.all().filter(id=book_id).exists():
            return HttpResponse(status=500)

        book = Book.objects.get(id=book_id)

        order = Order.objects.all().filter(user=request.user, is_finished=False)

        if order:
            # messages.success(request,"يوجد طلب مفتوح")
            old_order = Order.objects.get(user=request.user, is_finished=False)

            if OrderDetails.objects.all().filter(book_id=book_id, order=old_order).exists():
                orderDitailsExist = OrderDetails.objects.all().filter(book_id=book_id, order=old_order)
                orderDitailsExist2 = OrderDetails.objects.filter(book_id=book_id, order=old_order).update(
                    quantity=F('quantity') + qty, total_price=(F('quantity') + qty)*F('price'))
                
               

                # messages.success(request, "الكتاب موجود سابقا")

            else:
                new_order_details = OrderDetails.objects.create( book=book, order=old_order, price=book.price, quantity=qty)
                # messages.warning(request,"الكتاب غير موجود سابقا")



        else:
            # messages.warning(request,"لا يوجد طلب مفتوح")
            new_order = Order()
            new_order.user = request.user
            new_order.order_date =timezone.now()
            new_order.save()

            new_order_details = OrderDetails.objects.create(book=book,order=new_order,price=book.price,quantity=qty)

        
        return HttpResponse(status=200)
    return HttpResponse(status=500)


@login_required
def cart(request):
    context=None
    order= False
    order_books =False
    if Order.objects.all().filter(user=request.user, is_finished=False):
        order = Order.objects.get(user=request.user, is_finished=False)
        order_books = OrderDetails.objects.all().filter(order=order)
        
    context={
        'order': order,
        'order_books': order_books,

        "categories": Categories.objects.all().filter(publish=True),
        # "authors": Authors.objects.all().filter(publish=True),
        "publishers": Publishers.objects.all().filter(publish=True),
    }

    return render(request, 'orders/order.html', context)
    # return render(request, 'orders/order.html', {'orders': order, })


@login_required
def delete_from_cart(request):
    
    if 'orderDetails_id' in request.GET  and request.user.is_authenticated and not request.user.is_anonymous:
        

        orderDetails_id = request.GET['orderDetails_id']
        # في حال كان معرف تفاصيل الطلب غير صحيح
        if not OrderDetails.objects.all().filter(id=orderDetails_id).exists():
            return redirect('orders:cart')  # أعادة التوجيه لصفحة الطلبات
         
        ordelet = OrderDetails.objects.get(id=orderDetails_id) #تفاصيل الطلب المراد حذفها
        order_id = ordelet.order.id #رقم الطلب
        if Order.objects.filter(id=order_id, is_finished=False):                
            ordelet.delete()
            orderdetails = OrderDetails.objects.all().filter(order=order_id).count() #مجموع  تفاصل الطلب
            #في حال كان مجموع تفاصيل الطلب أقل من واحد (اي الطلب لا يحتوي على تفاصيل ) سيتم حذف الطلب
            if orderdetails<1:
                Order.objects.get(id=order_id).delete() # حذف الطلب
        return redirect('orders:cart') # أعادة التوجيه لصفحة الطلبات
        

    return HttpResponse(status=500)




@login_required
def delete_cart(request):
    
    if 'order_id' in request.GET  and request.user.is_authenticated and not request.user.is_anonymous:
        

        order_id = request.GET['order_id']
        # في حال كان معرف  الطلب غير صحيح
        if not Order.objects.all().filter(id=order_id).exists():
            return redirect('orders:cart')  # أعادة التوجيه لصفحة الطلبات
         
  
        
        if Order.objects.filter(id=order_id, is_finished=False): 
            Order.objects.get(id=order_id).delete() # حذف الطلب
        return redirect('/') # أعادة التوجيه لصفحة الطلبات
        

    return HttpResponse(status=500)



@login_required
def confirm_cart(request):
    
    if request.user.is_authenticated and not request.user.is_anonymous and 'gover' in request.GET  and 'phone' in request.GET  and 'address' in request.GET  and 'order_id' in request.GET  : 
        

        order_id = request.GET['order_id']
        gover = request.GET['gover']
        phone = request.GET['phone']
        address = request.GET['address']

        # في حال كان معرف  الطلب غير صحيح
        if not Order.objects.all().filter(id=order_id).exists():
            return redirect('orders:cart')  # أعادة التوجيه لصفحة الطلبات
         
  
        
        if Order.objects.filter(id=order_id, is_finished=False): 
            Order.objects.filter(id=order_id).update(phone=phone, adderess=address, gover=gover, is_finished=True)  # تحديث  الطلب
        return redirect('/') # أعادة التوجيه لصفحة الطلبات
        

    return HttpResponse(status=500)




def sendemail(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ah.36.kh@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/')

