from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPeopleView.as_view(), name='list_people'),
    path('create/', views.PeopleCreateView.as_view(), name='new_people'),
    path(
        'update/<int:pk>/',
        views.PeopleUpdateView.as_view(),
        name='update_people'
    ),
    path(
        'delete/<int:pk>/',
        views.PeopleDeleteView.as_view(),
        name='delete_people'
    ),
]
