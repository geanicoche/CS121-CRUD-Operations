from django.db import models

# Create your models here.

class Author(models.Model):
        first_name = models.CharField(max_length=100, null=True)
        last_name = models.CharField(max_length=100, null=True)
        origin = models.CharField(max_length=50, null=True)

        def __str__(self):
            return self.last_name + ", " + self.first_name

class Book(models.Model):
        title = models.CharField(max_length=100, null=True)
        author = models.ForeignKey(Author, on_delete=models.CASCADE)
        category = models.CharField(max_length=50, null=True)
        price = models.CharField(max_length=50, null=True)
        pages = models.IntegerField(null=True)
        language = models.CharField(max_length=50, null=True)

        def __str__(self):
            return self.title + " -- " + self.author.last_name + ", " + self.author.first_name
