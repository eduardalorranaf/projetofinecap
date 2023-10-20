from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User (AbstractUser):
    nome = models.CharField(_('Nome_de_usuário'), blank=True, max_length=255)
    first_name = None
    last_name = None