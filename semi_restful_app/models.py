from django.db import models

class Show(models.Model):
  title = models.CharField(max_length=80)
  network = models.CharField(max_length=50)
  release_date = models.DateField()
  desc = models.TextField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
