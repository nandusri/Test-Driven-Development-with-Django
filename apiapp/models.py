from django.db import models

# Create your models here.

class List(models.Model):
    """This class represents the list model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a readable representation of the model field."""
        return self.name

