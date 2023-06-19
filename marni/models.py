from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Création d'un utilisateur
def creer_utilisateur(username, password, email):
    try:
        user = User.objects.create_user(username=username, password=password, email=email)
        print("Utilisateur créé avec succès !")
        return user
    except Exception as e:
        print("Une erreur s'est produite lors de la création de l'utilisateur :", str(e))
        return None

# Appel de la fonction pour créer un utilisateur

