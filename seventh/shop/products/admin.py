from django.contrib import admin
from .models import ProductCategory, Product, Photo

from django.urls import path
from django.shortcuts import render
from django import forms


class CsvImportForm(forms.Form):
    csv_uploader = forms.FileField()


class PhotoAdd(admin.StackedInline):
    model = Photo
    fields = ("product", "add_photo")
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'quantity')
    list_display_links = ('id', 'name')
    inlines = [PhotoAdd]


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("product", "add_photo")


class ProductCategoryAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Photo, PhotoAdmin)
