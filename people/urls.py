from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPeopleView.as_view(), name='list_people'),
    path('create/', views.PeopleCreateView.as_view(), name='new_people')
]
