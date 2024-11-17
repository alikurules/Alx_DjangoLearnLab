from django.test import TestCase
from django.contrib.auth.models import User, Group
from app_name.models import Post

class PermissionsTestCase(TestCase):
    def setUp(self):
        # Create groups and permissions
        group = Group.objects.create(name="Editors")
        user = User.objects.create_user(username="editor", password="password")
        user.groups.add(group)

    def test_editor_can_create_post(self):
        self.client.login(username="editor", password="password")
        response = self.client.post('/create-post/', {'title': 'Test', 'content': 'Test Content'})
        self.assertEqual(response.status_code, 200)
