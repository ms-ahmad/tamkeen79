
from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Order, OrderDetails


# Register your models here.

class orderAdmin(admin.ModelAdmin):
    list_display = ("user","order_date",  "is_finished","phone", "adderess", "gover", )
    list_filter = ("order_date",  "is_finished", "gover", )

admin.site.register(Order, orderAdmin)
admin.site.register(OrderDetails)
