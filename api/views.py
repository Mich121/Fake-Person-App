from rest_framework import generics, permissions, viewsets
from django.views import generic
from django.shortcuts import get_object_or_404
from .serializers import PersonSerializer, PersonOnlineSerializer
from .models import Person, PersonOnlineData
from .forms import PersonCreateForm
import requests, json
from django.urls import reverse
from rest_framework import filters
from .pagination import PeopleListAPIPagination

# Create your views here.
class Home(generic.TemplateView):
    template_name = 'home.html'

class PersonCreate(generic.CreateView):
    model = Person
    template_name = 'create_person.html'
    form_class = PersonCreateForm
    
    def get_success_url(self):
        return reverse('person_create', kwargs={})

    def get_initial(self, *args, **kwargs):
        initial = super(PersonCreate, self).get_initial(**kwargs)
        url = 'https://pipl.ir/v1/getPerson'
        response = requests.get(url)
        data = response.json()
        initial['name'] = data['person']['personal']['name']
        initial['surname'] = data['person']['personal']['last_name']
        initial['certificate'] = data['person']['education']['certificate']
        initial['university'] = data['person']['education']['university']
        initial['marriage'] = data['person']['marriage']['married']
        initial['age'] = data['person']['personal']['age']
        initial['height'] = data['person']['personal']['height']
        initial['weight'] = data['person']['personal']['weight']
        initial['country'] = data['person']['personal']['country']
        initial['position'] = data['person']['work']['position']
        initial['salary'] = data['person']['work']['salary']
        initial['religion'] = data['person']['personal']['religion']
        return initial

class PersonListAPI(generics.ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'surname']
    pagination_class = PeopleListAPIPagination

class PersonDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Person, id=pk)

class PersonVS(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['age']

class PersonOnlineListAPI(generics.RetrieveAPIView):
    serializer_class = PersonOnlineSerializer

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(PersonOnlineData, person=pk)