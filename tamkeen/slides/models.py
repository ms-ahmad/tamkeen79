from django.db import models
from books.models import Authors, Categories, Publishers
# Create your models here.


class slides(models.Model):
    slide_name = models.CharField(("اسم السلايد"), max_length=50)
    img = models.ImageField(("الصورة"), upload_to="slides/%Y/%m-%d",  max_length=None)
    show = models.BooleanField(("يظهر"))

    class Meta:
        verbose_name = "السلايد"
        verbose_name_plural = "السلايدات"


    def __str__(self):
        return self.slide_name



class Comming_soon(models.Model):
    book_title=models.CharField(("اسم الكتاب"), max_length=50)
    pages = models.PositiveIntegerField(("عدد الصفحات"), blank=True, null=True)
 
    cover_book = models.ImageField(("صورة "), upload_to="books/covers/", blank=True, null=True)
    auther = models.ManyToManyField(Authors, verbose_name=("المؤلف"))
    price = models.PositiveIntegerField(
        verbose_name="السعر", blank=True, null=True)
 
    Categories = models.ManyToManyField(Categories, verbose_name=("الفئة"))

    Publishers = models.ManyToManyField(Publishers, verbose_name=("الناشر"))
    year_publish = models.DateField(
        ("سنة النشر"), auto_now_add=False, blank=True, null=True)

    description_book = models.TextField(
        ("مختصر عن الكتاب"), blank=True, null=True)
    publish = models.BooleanField(("يتم نشره"), default=False)

    created = models.DateField(
        ("تاريخ الإضافة"),  auto_now_add=True, null=True)

    def __str__(self):
        return self.book_title

    def y_publish(self):
        return self.year_publish.year

    def get_Categories(self):
        return " - ".join([b.name_category for b in self.Categories.all()])

    def get_Authors(self):
        return " - ".join([b.name_author for b in self.auther.all()])

    class Meta:
        verbose_name = "كتاب مترقب"
        verbose_name_plural = "كتب مترقبة"


class Quotes(models.Model):
    person=models.CharField(("القائل"), max_length=50)
    quotation = models.CharField(("الاقتباس أو القول"), max_length=250)
    image = models.ImageField(
        ("صورة الشخص"), upload_to="Quotes/%Y/%m-%d", height_field=None, width_field=None, max_length=None)
    pubish = models.BooleanField(("ينشر"))


    class Meta:
        verbose_name = "اقتباس"
        verbose_name_plural = "أقتباسات"


    def __str__(self) :
        return self.person
