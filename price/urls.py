from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.top, name="top"),
    path(r'add', views.add_task, name="add_task"),
    path(r'delete/<int:form_id>', views.delete, name="delete"),
    path(r'sort', views.sort, name="sort"),
]