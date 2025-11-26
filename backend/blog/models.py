from django.db import models
from django.contrib.auth.models import User


# создаем таблицу в базе данных и ее колонки
class Category(models.Model):
    # создание колонок в таблице 
    name = models.CharField(max_length=20) # создание STR поля с ограничением символов
    description = models.TextField(blank=True) # создание STR поля для большого количества текста

    # магический метод STR для получения строки из объекта
    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



    # One-to-Many - один автор - много постов
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # ForeignKey - Связь один ко многим 
    # on_delete=models.CASCADE - При удалении родителя удаляются дочерние записи
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    # on_delete=models.SET_NULL,null=True - при удалении родителя поле просто становится NULL


    # Many-to-Many много тегов много постов
    tags = models.ManyToManyField(Tag,blank=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"Комментарий от {self.author} для {self.post}"
    

