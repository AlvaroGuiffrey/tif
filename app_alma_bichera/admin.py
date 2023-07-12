from django.contrib import admin
from .models import Promo


# Register your models here.
@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    ...
