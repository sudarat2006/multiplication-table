from django.db import models

# Create your models here.
PREFIX_CHOICES =[
    ('นาย', 'นาย'),
    ('นาง', 'นาง'),
    ('นางสาว', 'นางสาว'),
    
]
class Student(models.Model):
    stid = models.IntegerField(unique=True)
    neme_prefix = models.CharField(choices=PREFIX_CHOICES, max_length=10)
    first_name = models.CharField(max_length=100)
    last_neme = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    
def __str__(self):
        return str(self.stid)
    