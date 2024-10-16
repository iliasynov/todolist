from django.urls import path
from .views import *

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('add/', add_todo, name='add_todo'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),  # New URL pattern

]
