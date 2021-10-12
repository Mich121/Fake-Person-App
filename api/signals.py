from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from api.models import Person, PersonOnlineData 

@receiver(post_save, sender = Person)
def create_persononlinedata(sender, instance, created, **kwargs):
    if created:
        url = 'https://pipl.ir/v1/getPerson'
        response = requests.get(url)
        data = response.json()
        PersonOnlineData.objects.create(person=instance, email=data['person']['online_info']['email'], ip_address=data['person']['online_info']['ip_address'])