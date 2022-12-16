from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #   نمایش نمودی از آبجکت هایی که از کلاس پست در پنل ادمین ساخته میشوند
    def __str__(self):
        return self.title
        # print(self.title)
        # print(self.author), self.author