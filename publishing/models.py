from django.db import models

# Create your models here.

class Book(models.Model):
    #kunci1 = models.CharField(max_length=55,primary_key=True)
    #kunci2 = models.CharField(max_length=55,unique=True)

    title = models.CharField(max_length=200)
    the_year = models.PositiveIntegerField(null=True,blank=True)
    synopsis = models.TextField(null=True,blank=True)
    author = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher',on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True) # diisi jika kosong
    modified = models.DateTimeField(auto_now=True) # selalu diisi

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)
    foto = models.ImageField(default = "pas_foto/default.jpg", upload_to = "pas_foto")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    logo = models.ImageField(default="simbol/deafult.jpg", upload_to = "simbol")

    def __str__(self):
        return self.name

class Preface(models.Model):
    book = models.OneToOneField('Book', on_delete=models.PROTECT)
    speech = models.TextField()

    def __str__(self):
        return str(self.book)
