from django.db import models

# Create your models here.


class Art(models.Model):
	artist = models.CharField(max_length=120, blank=True)
	title = models.CharField(max_length=120, blank=True)
	url = models.CharField(max_length=400, blank=True)
	size = models.CharField(max_length=120, blank=True)
	medium = models.CharField(max_length=120, blank=True)
	price = models.IntegerField(default=0)