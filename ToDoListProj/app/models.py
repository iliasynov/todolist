from django.db import models
from django.conf import settings  # Add this import

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)  # New field to associate Todo with a user

    def __str__(self):
        return self.title

