from django.db import models

from core.models import Activity

# Create your models here.

class Tags(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(unique=True)
	activity = models.ManyToManyField(Activity,blank=True,default=None)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title
	class Meta:
		verbose_name = "Tags"
		verbose_name_plural = "Tags"