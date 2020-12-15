from django.db import models
from datetime import date, datetime


class ShowManager(models.Manager):
  def getErrors(self, postData):

    today = date.today()
    
    errors = {}
    
    # title at least 2 chars
    if len(postData['title']) < 2:
      errors['title'] = 'title should be at least 2 characters'
    
    if len(postData['network']) < 3:
      errors['network'] = 'Networks should be at least 3 characters'
      
    if len(postData['desc']) > 0 and len(postData['desc']) < 10:
      errors['desc'] = 'Description should be EMPTY OR at least 10 characters'
    
    if postData['release_date'] > str(today):
      errors['release_date'] = 'Date should be in the PAST'
    
    if postData['isNew'] == 'True':
      all_titles = Show.objects.all()
      for show in all_titles:
        if postData['title'] == show.title:
          errors['title'] = 'Title must be unique'
          return errors
    return errors

class Show(models.Model):
  title = models.CharField(max_length=80)
  network = models.CharField(max_length=50)
  release_date = models.DateField()
  desc = models.TextField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = ShowManager()
