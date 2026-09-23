from django.contrib import admin
from .models import Product,Variation

class productAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}

class variationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')


admin.site.register(Product,productAdmin)
admin.site.register(Variation,variationAdmin)
