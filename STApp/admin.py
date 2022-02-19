from django.contrib import admin
from STApp.models import GalaryModel
# Register your models here.

class GalaryAdmin(admin.ModelAdmin):
    list_display = ['pics', 'title', 'price']




admin.site.register(GalaryModel, GalaryAdmin)