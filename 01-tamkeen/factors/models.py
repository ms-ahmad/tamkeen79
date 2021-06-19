from django.db import models
from django.db.models.fields.related import ManyToManyField
from account.models import User
from books.models import Book
from django.db.models import Avg, Count, Min, Sum


# Create your models here.

class Factor(models.Model):
    # user_id = models.ManyToManyField(User, verbose_name="صاحب الطلب", blank=True)
    id_user = models.ForeignKey(User, verbose_name=("صاحب الطلب"), on_delete=models.SET_NULL, null=True)
    created = models.DateField(("تاريخ الإضافة"),  auto_now_add=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="السعر", blank=True, null=True)
    is_send = models.BooleanField(("تم التأكيد"),default=False)
    is_closed = models.BooleanField(("إغلاق"),default=False,help_text="في حال تم ارسال الطلبية لصاحبها ")
    # total = models.Sum('books__detail_price')

    # def __str__(self):
    #     return self.user_id.

    class Meta:
        verbose_name = "الطلبية"
        verbose_name_plural = "الطلبيات"
    

    def __str__(self) :
        return f"({self.pk}) => {self.created} "


class Factor_Detailes(models.Model):
    book_id = models.ManyToManyField(Book, verbose_name="الكتاب",related_name="books")
    
    factor_id = models.ForeignKey(Factor, verbose_name=("الطلبية"), null=True, on_delete=models.SET_NULL, related_name="factors")
    book_count = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="العدد", default=1)
    detail_price = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="مجموع السعر", )

    class Meta:
        verbose_name = "تفاصيل الطلبية"
        verbose_name_plural = "تفاصيل الطلبيات "

    def get_booktitle(self):
        return " - ".join([b.title_book for b in self.book_id.all()])

    def __str__(self):
        return self.get_booktitle()




