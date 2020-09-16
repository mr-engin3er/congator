from django.contrib import admin
from .models import Search
# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Search)
