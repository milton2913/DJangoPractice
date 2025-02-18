from django.db import models

# Create your models here.
class pages(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=150)
    description=models.TextField()