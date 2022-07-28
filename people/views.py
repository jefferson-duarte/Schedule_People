from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import People
from .forms import PeopleForm


class ListPeopleView(ListView):
    model = People
    queryset = People.objects.all().order_by('full_name')

    def get_queryset(self):
        qs = super().get_queryset()
        filter_name = self.request.GET.get('name') or None

        if filter_name:
            qs = qs.filter(full_name__contains=filter_name)

        return qs


class PeopleCreateView(CreateView):
    model = People
    form_class = PeopleForm
    success_url = '/people/'


class PeopleUpdateView(UpdateView):
    model = People
    form_class = PeopleForm
    success_url = '/people/'


class PeopleDeleteView(DeleteView):
    model = People
    success_url = '/people/'
