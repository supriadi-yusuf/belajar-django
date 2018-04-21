from django.contrib import admin

#from publishing.models import Author, Publisher, Book, Preface
from .models import Author, Publisher, Book, Preface

# Register your models here.

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Preface)
