from django.urls import path
from .views import *

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('add/', add_todo, name='add_todo'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),  # New URL pattern
    path('toggle/<int:todo_id>/', toggle_todo_completion, name='toggle_todo_completion'),  # New URL pattern
    path('register/', register, name='register'),  # Registration URL
    path('accounts/login/', login_view, name='login'),  # Login URL
    path('logout/', logout_view, name='logout'),  # Logout URL
]
