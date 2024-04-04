from mvtu.myapp5 import admin
from mvtu.myapp5.models import Category, Product


@admin.action(description='Сбросить кол-во в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)



class ProductAdmin(admin.ModelAdmin):
    '''Списки продуктов'''
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', 'quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['name', 'description']
    search_help_text = ['Поиск по полю описания продукта (description)']
    actions = [reset_quantity]

