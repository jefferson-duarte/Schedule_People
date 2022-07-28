from django.forms import ModelForm
from .models import People


class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ['full_name', 'birth_date', 'active']
