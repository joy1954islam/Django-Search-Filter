from django.contrib import admin

# Register your models here.
from .models import Language,Entry

admin.site.register(Language)
admin.site.register(Entry)