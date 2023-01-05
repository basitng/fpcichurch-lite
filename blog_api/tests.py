from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category

class PostTests(APITestCase):
    
    def test_view_posts(self):
        url = reverse("blog_api:listcreate")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_post(self):
        url = reverse("blog_api:listcreate")
        self.testuser = User.objects.create_user(username="basitng", password="123456789")
        self.test_category = Category.objects.create(name="Django")

        data = {
            "title": "New",
            "author": 1,
            "excerpt": "New",
            "content": "New",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)