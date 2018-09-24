from django.contrib import admin

from .models import SupplierAccount

admin.site.register(SupplierAccount)

# class SupplierAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug":('name',)}
#     class Meta:
#         model = SupplierAccount

# admin.site.register(SupplierAccount,SupplierAdmin)