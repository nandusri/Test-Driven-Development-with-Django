from django.test import TestCase
from .models import List

# Create your tests here.
class ModelTestCase(TestCase):
    """This class defines the test suite for the list model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.list_name = "Write world class code"
        self.list = List(name=self.list_name)

    def test_model_can_create_a_list(self):
        """Test the bucketlist model can create a list."""
        old_count = List.objects.count()
        self.list.save()
        new_count = List.objects.count()
        self.assertNotEqual(old_count, new_count)
