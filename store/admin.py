from django.contrib import admin
from .models import Product, Variation, ProductGallery, Review
# import admin_thumbnails

# Register your models here.


# @admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock',
                    'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'status')


admin.site.register(Product, ProductAdmin)


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'variation_category',
                    'variation_value', 'is_active',)
    list_editable = ('is_active',)


admin.site.register(Variation, VariationAdmin)
admin.site.register(ProductGallery)
admin.site.register(Review, ReviewAdmin)
