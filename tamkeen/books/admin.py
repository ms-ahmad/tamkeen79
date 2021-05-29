from django.contrib import admin
from .models import Stores, Authors, Publishers, Categories, Book

# Register your models here.


class StoreAdmin(admin.ModelAdmin):
    list_display = ("name_store", "phone_store", "site_store", "publish",)
    list_editable = ("publish",)
    search_fields = ("name_store", "phone_store", "site_store", "address_store","description_store",)
    list_filter = ("publish", "created")


admin.site.register(Stores, StoreAdmin)


class AuthorAdmin(admin.ModelAdmin):
    # list_editable = ("name_author", "photo_author")
    list_display = ("name_author", "photo_author", "publish",)
    list_editable = ("publish",)
    list_filter = ("publish", "created")
    search_fields = ("name_author", "brief_about_author",)


admin.site.register(Authors, AuthorAdmin)


class PublisherAdmin(admin.ModelAdmin):

    list_display = ("name_publisher", "phone_publisher","logo_publisher", "publish",)
    list_editable = ("publish",)
    list_filter = ("publish", "created",)
    search_fields = ("name_publisher", "phone_publisher","address_publisher","site_publisher",)


admin.site.register(Publishers, PublisherAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name_category", "photo_category", "publish",)
    list_editable = ("publish",)
    list_filter = ("publish", "created")
    search_fields = ("name_category", "brief_about_category",)


admin.site.register(Categories, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):

    list_display = ("title_book",   "available", "y_publish",
                    "get_Categories", "publish", "showinSlideShow",)
    list_editable = ("available", "publish", "showinSlideShow",)
    list_filter = ("publish", "created", "year_publish", "available", "Categories","stores","Publishers",)
    search_fields = ("title_book", "auther", "description_book", )


admin.site.register(Book, BookAdmin)
