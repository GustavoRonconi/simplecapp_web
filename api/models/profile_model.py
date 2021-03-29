from django.contrib.auth.models import User
from django.db import models


class ProfileModel(models.Model):
    class Meta:
        db_table = "profile_user"

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    gender = models.BooleanField()
    date_of_birth = models.DateField(null=False)
    occupation = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, null=False, unique=True)
    cpf = models.CharField(null=False, max_length=50, unique=True)
    state = models.ForeignKey("StatesModel", null=False, on_delete=models.PROTECT)
    cep = models.CharField(null=False, max_length=50)
    street = models.CharField(max_length=50, null=False)
    district = models.CharField(max_length=50, null=False)

