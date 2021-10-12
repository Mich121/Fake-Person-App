from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    certificate = models.CharField(max_length=20)
    university = models.CharField(max_length=100)
    marriage = models.BooleanField()
    age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    height = models.FloatField()
    weight = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.CharField(max_length=15)
    religion = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.surname

class PersonOnlineData(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='person')
    email = models.EmailField(max_length=50)
    ip_address = models.CharField(max_length=40)

    def __str__(self):
        return self.person.name + ' ' + self.person.surname