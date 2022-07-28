from django.contrib import admin
from .models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = [
        'full_name', 'birth_date', 'active',
    ]

    list_editable = [
        'birth_date', 'active',
    ]
