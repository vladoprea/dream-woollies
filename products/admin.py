from django.contrib import admin
from .models import Product, Collection, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'on_sale',
        'price',
        'discount_price',
        'height',
        'width',
        'image',
    )

    ordering = ('sku',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user',
                    'subject', 'review',
                    'rate', 'created_at'
                    )

    readonly_fields = ('subject', 'review')

admin.site.register(Product, ProductAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Review, ReviewAdmin)


