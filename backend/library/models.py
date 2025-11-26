from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField()
    birth_day = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=12,unique=True)


    # Many-to-many - у книги может быть несколько авторов 
    author = models.ManyToManyField(Author)
    
    def __str__(self):
        return self.title
    
class BookCopy(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    publishing_house = models.ForeignKey(User,on_delete=models.CASCADE)
    publishing_house_date = models.DateField()
    copy_number = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.book.title
    
