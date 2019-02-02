from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

class Message(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	teacher = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

