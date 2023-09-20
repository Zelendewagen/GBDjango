from django.contrib import admin
from myapp.models import User, Author, Order, Post, Product


# Register your models here.

@admin.action(description="Сбросить колличество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'quantity']
    ordering = ['price', '-quantity']
    list_filter = ['price']
    search_fields = ['description']
    search_help_text = 'Поиск по описанию'
    actions = [reset_quantity]

    # fields = ['name', 'price', 'quantity']
    readonly_fields = ['name', 'price']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное '
                               'описание',
                        'fields':['description'],
        },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
    ]


admin.site.register(User)
admin.site.register(Author)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
admin.site.register(Post)
