from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.validators import cpf_validator

# Create your models here.
class CustomUser(AbstractUser):
    telephone = models.CharField(_('Telephone'),unique=True,max_length=32)
    cpf = models.CharField(unique=True,validators=[cpf_validator],max_length=16)

    REQUIRED_FIELDS = ['email','cpf','telephone']