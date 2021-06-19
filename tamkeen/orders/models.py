from django.db import models
# from account.models import User
from django.contrib.auth.models import User
from books.models import Book
# Create your models here.


class Order(models.Model):
    goverment = [
        ('b', 'بغداد'),
        ('m', 'محافظات'), 
    ]

    user=models.ForeignKey(User, verbose_name=("صاحب الطلب"), on_delete=models.SET_NULL,null=True)
    order_date = models.DateTimeField(("التاريخ"), auto_now_add=True, null=True)
    details = models.ManyToManyField(Book, through='OrderDetails', verbose_name=(""))
    is_finished = models.BooleanField(("التأكيد"), default=False)
    phone = models.PositiveIntegerField(("الهاتف"), blank=True, null=True)
    adderess= models.CharField(("العنوان"), max_length=250,blank=True,null=True)
    gover = models.CharField(("المحافظة"), max_length=1, choices=goverment, blank = True, null = True)


    def __str__(self) :
        return f' {self.user.username}  {self.id}'


class OrderDetails(models.Model):
    book = models.ForeignKey(Book, verbose_name=("الكتاب"), on_delete=models.CASCADE)
    order = models.ForeignKey(Order, verbose_name=("الطلب"), on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name="السعر", blank=True, null=True)
    total_price = models.PositiveIntegerField(verbose_name="مجموع السعر", blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name="العدد", blank=True, null=True)


    def __str__(self) :
        return f'{self.book.title_book} ({self.order.id})'



    def save(self, *args, **kwargs):
        self.total_price = int(self.quantity) * int(self.price)
        super(OrderDetails, self).save(*args, **kwargs)









