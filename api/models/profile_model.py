from django.contrib.auth.models import User
from django.db import models


class ProfileModel(models.Model):
    class Meta:
        db_table = "profile_user"

    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE) #TODO AGORA OS PERFIS PODEM OU NÃO TER USUARIOS
    gender = models.BooleanField()
    date_of_birth = models.DateField()
    occupation = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=50, unique=True)
    state = models.ForeignKey("StatesModel", on_delete=models.PROTECT)
    cep = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
