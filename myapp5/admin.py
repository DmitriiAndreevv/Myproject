from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.action(description='Сбросить кол-во в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)
class ProductAdmin(admin.ModelAdmin):
    '''список продуктов'''
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['name', 'description']
    search_help_text = 'Поиск по полю Описанию продукта (description)'
    actions = [reset_quantity]

    '''Отдельный продукт'''
    # fields = ['name', 'category', 'quantity', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']

    fieldsets = [
        (
            None,
            {
                'classes' : ['wide'],
                'fields' : ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes' : ['collapse'],
                'description' : 'Категория товара и его подробное описание',
                'fields' : ['description', 'category'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields' : ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочие',
            {
                'description' : 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields' : ['date_added', 'rating'],
            }
        ),
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
