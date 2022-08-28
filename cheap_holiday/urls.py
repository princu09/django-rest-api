from django.contrib import admin
from django.urls import path, include
from tour import urls

admin.site.site_header = "Cheap Holiday"
admin.site.index_title = "Welcome to Cheap Holiday"

urlpatterns = [
    path('siteAdminApproveBySamcom/', admin.site.urls),
    path('', include('tour.urls')),
]