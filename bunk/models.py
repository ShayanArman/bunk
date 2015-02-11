from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Bunk(models.Model):
	from_user = models.ForeignKey(User, related_name="bunk_from_related")
	to_user = models.ForeignKey(User, related_name="bunk_to_related")
	bunk_time = models.DateTimeField(
		default=timezone.now)

	@classmethod
	def create_user(cls, from_user, to_user):
		return cls.objects.create(from_user=from_user, to_user=to_user)


class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	photo = models.ImageField(upload_to='static/')