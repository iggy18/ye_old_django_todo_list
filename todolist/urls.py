from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete_todo/<todo_id>', views.delete_todo, name='delete_todo'),
]