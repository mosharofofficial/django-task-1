from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    dept = models.CharField(max_length=50)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    dept = models.CharField(max_length=50)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    email = models.EmailField()
    dept = models.CharField(max_length=50)
