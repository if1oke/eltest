from django.contrib import admin

from .models import Brand, Car, CarTTX, Comment, Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = list_display
    list_editable = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country']
    search_fields = ['id', 'name']
    list_filter = ['country']
    list_editable = ['name']
    raw_id_fields = ['country']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand', 'year_release', 'year_completion',
                    'base_price']
    search_fields = ['id', 'name']
    list_filter = ['year_release', 'year_completion', 'base_price']
    raw_id_fields = ['brand']


@admin.register(CarTTX)
class CarTTXAdmin(admin.ModelAdmin):
    list_display = ['id', 'car', 'door', 'engine', 'cylinder', 'kpp']
    search_fields = ['id']
    list_filter = ['door', 'cylinder', 'kpp']
    raw_id_fields = ['car']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'car', 'pub_date', 'text']
    search_fields = ['id', 'author__username']
    raw_id_fields = ['author', 'car']

    def get_text(self, comment):
        return comment.text[:10]
