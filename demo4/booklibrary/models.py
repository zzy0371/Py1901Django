from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentUser(User):
    college = models.CharField(max_length=20,blank=True,null=True)
    num = models.IntegerField(blank=True,null=True)

class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20,blank=True,null=True)
    publish_com = models.CharField(max_length=20,null=True,blank=True)
    publish_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name

class History(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    studentuser = models.ForeignKey(StudentUser,on_delete=models.CASCADE)
    date_borrow = models.DateTimeField(auto_now_add=True)
    date_return = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.studentuser.username + '  借   <<' +self.book.name + ">>"


