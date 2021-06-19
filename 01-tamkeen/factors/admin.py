from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Factor, Factor_Detailes
# Register your models here.



class factordetailInline(admin.TabularInline):
    model = Factor_Detailes

class factorAdmin(admin.ModelAdmin):
    list_display=["id_user", "created", "price", "is_closed", ]
    list_filter = ["id_user", "created", "is_closed", ]

    inlines=[factordetailInline]



class factor_detailesAdmin(admin.ModelAdmin):
    list_display = ["get_booktitle", "factor_id","book_count", "detail_price", ]
    # list_filter = ["get_booktitle", "created", "is_closed", ]





admin.site.register(Factor, factorAdmin)
# admin.site.register(Factor)
admin.site.register(Factor_Detailes, factor_detailesAdmin)

