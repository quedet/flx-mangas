from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from apps.core.models import Category


# Create your models here.
class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"
        RATHER_NOT_SAY = "RATHER_NOT_SAY", "Rather not to say"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField(default=now)
    avatar = models.ImageField(null=True, blank=True, upload_to='profiles/avatars')
    gender = models.CharField(max_length=25, choices=Gender.choices)
    interests = models.ManyToManyField(Category, symmetrical=False)

