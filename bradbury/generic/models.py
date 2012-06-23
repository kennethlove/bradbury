from django.db import models
from django.contrib.auth.models import User

from userena.models import UserenaBaseProfile

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User, related_name="profile")
