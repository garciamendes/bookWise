# Django
from django.contrib import admin

# Local
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user__email']


admin.site.register(Profile, ProfileAdmin)
