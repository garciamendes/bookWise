# Django
from django.contrib import admin

# Local
from .models import (
    Book,
    BookRating
)


class BookAdmin(admin.ModelAdmin):
    list_display = ['author', 'total_pages']
    search_fields = ['author']
    list_filter = ['categories']


class BookRatingAdmin(admin.ModelAdmin):
    list_display = ['uid', 'book', 'rating']
    search_fields = ['book']


admin.site.register(Book, BookAdmin)
admin.site.register(BookRating, BookRatingAdmin)
