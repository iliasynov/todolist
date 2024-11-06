from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Todo

# Create your tests here.


class TodoAppTests(TestCase):

    def setUp(self):
        # Set up the test client and create a test user
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.todo = Todo.objects.create(title='Test Todo', user=self.user, completed=False)

    def test_todo_list_authenticated_user(self):
        # Log in the user
        self.client.login(username='testuser', password='testpass')

        # Access the todo_list page
        response = self.client.get(reverse('todo_list'))

        # Check the status code and that the correct template is used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_list.html')

        # Check that only this user's todos are listed
        self.assertContains(response, 'Test Todo')
        self.assertEqual(len(response.context['todos']), 1)

    def test_add_todo_authenticated_user(self):
        # Log in the user
        self.client.login(username='testuser', password='testpass')

        # Add a new todo
        response = self.client.post(reverse('add_todo'), {'title': 'New Todo'})

        # Check that the todo was created
        self.assertEqual(Todo.objects.filter(user=self.user).count(), 2)
        self.assertRedirects(response, reverse('todo_list'))

    def test_delete_todo_authenticated_user(self):
        # Log in the user
        self.client.login(username='testuser', password='testpass')

        # Delete the test todo
        response = self.client.post(reverse('delete_todo', args=[self.todo.id]))

        # Check that the todo was deleted
        self.assertEqual(Todo.objects.filter(user=self.user).count(), 0)
        self.assertRedirects(response, reverse('todo_list'))

    def test_toggle_todo_completion(self):
        # Log in the user
        self.client.login(username='testuser', password='testpass')

        # Toggle completion status
        response = self.client.post(reverse('toggle_todo_completion', args=[self.todo.id]))
        self.todo.refresh_from_db()

        # Verify completion was toggled
        self.assertTrue(self.todo.completed)
        self.assertRedirects(response, reverse('todo_list'))





