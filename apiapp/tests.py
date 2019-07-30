from django.test import TestCase
from .models import List
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

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

    def test_api_can_get_a_list(self):
        """Test the api can get a given list."""
        bucketlist = List.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': bucketlist.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_list(self):
        """Test the api can update a given bucketlist."""
        change_bucketlist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_list(self):
        """Test the api can delete a bucketlist."""
        bucketlist = List.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
