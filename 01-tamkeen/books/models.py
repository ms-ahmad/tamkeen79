from django.db import models
from account.models import User
from django.utils import timezone
import datetime
from django.utils.text import slugify


# Create your models here.


class Stores(models.Model):
    name_store = models.CharField(max_length=255, verbose_name="اسم المتجر")
    # slug = models.SlugField(max_length=20, allow_unicode=True ,null=True)
    address_store = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="عنوان المتجر")
    phone_store = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="الهاتف")
    # phone_store = PhoneNumberField(blank=True, null=True, verbose_name="الهاتف")
    site_store = models.URLField(
        max_length=255, verbose_name="موقع المتجر", blank=True, null=True)
    logo_store = models.ImageField(
        upload_to='stores/logos/', verbose_name="الشعار", blank=True, null=True)
    description_store = models.CharField(
        max_length=255, verbose_name="نبذة عن المتجر", blank=True, null=True)
    dirctors_store = models.ManyToManyField(User, verbose_name="المدراء", blank=True)
    publish = models.BooleanField(("يتم نشره"), default=False)
    created = models.DateField( ("تاريخ الإضافة"),  auto_now_add=True, null=True)


    def __str__(self):
        return self.name_store

    # def save(self, *args, **kwargs):
    #     value = self.name_store
    #     self.slug = slugify(value, allow_unicode=True)
    #     super().save(*args, **kwargs)



    class Meta:

        verbose_name_plural = "المتاجر"
        verbose_name = "متجر"


class Authors(models.Model):
    name_author = models.CharField(("اسم المؤلف"), max_length=50)
    brief_about_author = models.CharField(
        ("نبذه عن المؤلف"), max_length=255, blank=True, null=True)
    photo_author = models.ImageField(
        ("صورة"), upload_to="authors/photo/",  blank=True, null=True)
    publish = models.BooleanField(("يتم نشره"), default=False)
    created = models.DateField(
        ("تاريخ الإضافة"),  auto_now_add=True, null=True)

    def __str__(self):
        return self.name_author

    class Meta:
        verbose_name = "مؤلف"
        verbose_name_plural = "مؤلفين"


class Publishers(models.Model):
    name_publisher = models.CharField(("اسم دار النشر"), max_length=50)
    address_publisher = models.CharField(
        ("العنوان"), max_length=255, blank=True, null=True)
    phone_publisher = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="الهاتف")
    site_publisher = models.URLField(
        ("الموقع"), max_length=200, blank=True, null=True)
    logo_publisher = models.ImageField(
        ("الشعار"), upload_to="publishers/logos/",  blank=True, null=True)
    publish = models.BooleanField(("يتم نشره"), default=False)
    created = models.DateField(
        ("تاريخ الإضافة"),  auto_now_add=True, null=True)

    def __str__(self):
        return self.name_publisher

    class Meta:
        verbose_name = "دار النشر"
        verbose_name_plural = "دور النشر"


class Categories(models.Model):
    name_category = models.CharField(("اسم الفئة"), max_length=50)
    brief_about_category = models.CharField(
        ("نبذه عن الفئة"), max_length=255, blank=True, null=True)
    photo_category = models.ImageField(
        ("صورة"), upload_to="categories/photo/",  blank=True, null=True)
    publish = models.BooleanField(("يتم نشره"), default=False)
    created = models.DateField(
        ("تاريخ الإضافة"),  auto_now_add=True, null=True)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "فئة"
        verbose_name_plural = "الفئات"


class Book(models.Model):
    title_book = models.CharField(("اسم الكتاب"), max_length=200)
    cover_book = models.ImageField(
        ("صورة "), upload_to="books/covers/", blank=True, null=True)
    auther = models.ManyToManyField(Authors, verbose_name=("المؤلف"))
    price = models.PositiveIntegerField(verbose_name="السعر", blank=True, null=True)
    pages = models.PositiveIntegerField(("عدد الصفحات"), blank=True, null=True)
    values = models.PositiveIntegerField(
        ("عدد الاجزاء"), blank=True, null=True, default=1)
    Categories = models.ManyToManyField(Categories, verbose_name=("الفئة"))
    stores = models.ManyToManyField(Stores, verbose_name=("المتجر"), related_name="store_book",)
    Publishers = models.ManyToManyField(Publishers, verbose_name=("الناشر"))
    year_publish = models.DateField(
        ("سنة النشر"), auto_now_add=False, blank=True, null=True)

    description_book = models.TextField( ("مختصر عن الكتاب"), blank=True, null=True)
    available = models.BooleanField(("متوفر"), default=True)
    publish = models.BooleanField(("يتم نشره"), default=False)
    showinSlideShow = models.BooleanField(("يظهر في السلايد"), default=False)
    created = models.DateField(
        ("تاريخ الإضافة"),  auto_now_add=True, null=True)

    def __str__(self):
        return self.title_book

    def y_publish(self):
        return self.year_publish.year

    def showpic(self):
        return f"<img src='{self.cover_book.url}'>"

    def get_Categories(self):
        return " - ".join([b.name_category for b in self.Categories.all()])

    def get_Authors(self):
        return " - ".join([b.name_author for b in self.auther.all()])
    
    def get_Publishers(self):
        return " - ".join([b.name_publisher for b in self.Publishers.all()])


 

    def get_Stores(self):
        return " - ".join([b.name_store for b in self.stores.all()])



    class Meta:
        verbose_name = "كتاب"
        verbose_name_plural = "كتب"
