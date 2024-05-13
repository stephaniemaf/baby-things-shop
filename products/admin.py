from django.contrib import admin
from .models import Category, Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ReviewAdmin(admin.ModelAdmin):

    list_filter = ('approved', 'pub_date')
    list_display = ('name','body', 'approved', 'pub_date','content_type')
    search_fields = ('user','body')
    actions = ['approve_reviews']

    def content_type(self, obj):
        content_type.short_description = 'Content Type'
    
    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)

