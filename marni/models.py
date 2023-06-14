from django.db import models
from django.contrib.auth.models import User, AbstractUser


from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    password = models.EmailField()
    # Autres champs de votre modèle...
