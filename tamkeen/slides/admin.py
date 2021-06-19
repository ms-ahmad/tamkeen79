from django.contrib import admin
from .models import slides, Comming_soon, Quotes
# Register your models here.


class SlidesAdmin(admin.ModelAdmin):
    list_display = ("slide_name", "img", "show", )
    list_editable = ( "img", "show",)
    search_fields = ("slide_name",)
    list_filter = ("show", )


admin.site.register(slides, SlidesAdmin)


class Comming_soon_Admin(admin.ModelAdmin):

    list_display = ("book_title", "y_publish","get_Categories", "publish", )
    list_editable = ( "publish", )
    list_filter = ("publish", "created", "year_publish",
                    "Categories",  "Publishers",)
    search_fields = ("book_title", "auther", "description_book", )


admin.site.register(Comming_soon, Comming_soon_Admin)


class Quotes_Admin(admin.ModelAdmin):

    list_display = ("person", "quotation", "image", "pubish", )
    list_editable = ("quotation", "image", "pubish", )
    list_filter = ("pubish",)
    search_fields = ("person", "quotation", )


admin.site.register(Quotes, Quotes_Admin)




