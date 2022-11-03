from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from tinymce import models as tinymce_models

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  portfolio = tinymce_models.HTMLField()

  def __str__(self):
    return f'{self.user} ({self.user.first_name} {self.user.last_name})'


class Exhibition(models.Model):
  title = models.CharField(max_length=120)
  url = models.CharField(max_length=120)
  artists = models.ManyToManyField(User)
  description = tinymce_models.HTMLField()
  
  def __str__(self):
    return f'{self.title} - {self.url}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()
