from django.views.generic import ListView, CreateView
from .models import People
from .forms import PeopleForm


class ListPeopleView(ListView):
    model = People
    queryset = People.objects.all().order_by('full_name')


class PeopleCreateView(CreateView):
    model = People
    form_class = PeopleForm
    success_url = '/people/'
