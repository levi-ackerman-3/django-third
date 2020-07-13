from django.db import models

# Create your models here.
class todoadder(models.Model):
    task=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.task