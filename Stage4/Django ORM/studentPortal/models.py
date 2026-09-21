from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Branch(models.TextChoices):
        CSE = "CSE", "Computer Science"
        IT = "IT", "Information Technology"
        CE = "CE", "Civil Engineering"
        ME = "ME", "Mechanical Engineering"
        EC = "EC", "Electronics & Communication"
class Student(models.Model):
    name = models.CharField(max_length=100,null=False)
    
    enrollment = models.CharField(unique=True,max_length=16,null=False)
    
    age = models.PositiveIntegerField(null=False,
        validators=[
                    MinValueValidator(1),
                    MaxValueValidator(100),
            ])
    
    branch = models.CharField(
        max_length=3,
        choices=Branch.choices,
        null=False
    )
    
    passout_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(2100),
    ]
    )
    def __str__(self):
        return self.name
    
    