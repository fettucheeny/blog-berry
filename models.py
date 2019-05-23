from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	title = models.CharField(verbose_name="Post Title", max_length=140)
	text = models.TextField()
	publish_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Comment(models.Model):
    user = models.CharField(max_length=60)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)