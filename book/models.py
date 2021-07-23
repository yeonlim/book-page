from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Book(models.Model):
  title = models.CharField(max_length=200)
  writer = models.CharField(max_length=100)
  p_date = models.DateTimeField()
  contents = models.TextField()
  img = models.ImageField(upload_to="book/", blank=True, null=True)
  img_thumbnail = ImageSpecField(source='img', processors=[ResizeToFill(350, 500)])
 
  def __str__(self):
    return self.title

  def summary(self):
    return self.contents[:100]
