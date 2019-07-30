from django.test import TestCase
from .models import List
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines the test suite for the list model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.list_name = "Write world class code"
        self.list = List(name=self.list_name)

    def test_model_can_create_a_list(self):
        """Test the list model can create a list."""
        old_count = List.objects.count()
        self.list.save()
        new_count = List.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.list_data = {'name': ''}
        self.response = self.client.post(
            reverse('create'),
            self.list_data,
            format="json")

    def test_api_can_create_a_list(self):
        """Test the api"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
