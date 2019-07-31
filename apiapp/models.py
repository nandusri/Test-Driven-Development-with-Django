from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    """This class represents the list model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey('auth.User',related_name='bucketlists',on_delete=models.CASCADE) 
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a readable representation of the model field."""
        return self.name

