from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe


from product.models import Category, Brand, Product, ProductLine, ProductImage


# # Register your models here.


# class ProductLineInline(admin.TabularInline):
#     model = ProductLine


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductLineInline]


# admin.site.register(Category)
# admin.site.register(Brand)
# admin.site.register(ProductLine)


class EditLinkInLine(object):
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk],
        )

        if instance.pk:
            link = mark_safe(f"<a href='{url}'>edit</a>")
            return link
        else:
            return ""


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductLineInline(EditLinkInLine, admin.TabularInline):
    model = ProductLine
    readonly_fields = ("edit",)


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductLineInline,
    ]


class ProductLineAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(ProductLine, ProductLineAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
