from django.contrib import admin
from .models import *

admin.site.register(Report)

# @admin.register(Report)
# class SongAdmin(admin.ModelAdmin):
#     list_display = ('title', 'Type',)
#     list_filter = ('Type', 'date')
#     search_fields = ('title', 'Type',)