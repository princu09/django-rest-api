from django.contrib import admin
from .models import Tour
from import_export.admin import ImportExportModelAdmin

@admin.register(Tour)
class ModelAdmin(ImportExportModelAdmin):
       pass