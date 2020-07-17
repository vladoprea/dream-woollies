from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('orderitem_total', )


class OrderAdmin(admin.ModelAdmin):
    """
    Sets up read only fields that are automatically calculated
    so noone could change them. Orders list by date
    """
    inlines = (OrderLineItemAdminInLine, )
    readonly_fields = ('order_number', 'date', 'delivery_cost',
                        'order_total', 'grand_total')
    
    ordering = ('-date', )

admin.site.register(Order, OrderAdmin)
