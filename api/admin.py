from django.contrib import admin
from .models import Person, PersonOnlineData

# Register your models here.
admin.site.register(Person)
admin.site.register(PersonOnlineData)