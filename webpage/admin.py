from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['stid', 'neme_prefix', 'first_name', 'last_neme']
    search_fields = ['first_name', 'last_neme']    
    