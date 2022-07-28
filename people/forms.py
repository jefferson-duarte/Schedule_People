from django.forms import DateField, ModelForm, TextInput
from .models import People


class PeopleForm(ModelForm):
    birth_date = DateField(
        widget=TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = People
        fields = ['full_name', 'birth_date', 'active']
