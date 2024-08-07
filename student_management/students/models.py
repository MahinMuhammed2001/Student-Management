from django.db import models
from django.utils import timezone


    
class Course(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField()
    email= models.EmailField(unique=True)
    number= models.CharField(max_length=12)
    enrollment_date= models.DateField(default=timezone.now)
    course=models.ForeignKey(Course,on_delete=models.CASCADE, related_name='students')
    

    def __str__(self):
        return self.name