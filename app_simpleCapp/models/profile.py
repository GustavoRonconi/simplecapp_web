from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.PROTECT)
    age = models.IntegerField(null=False)
    gender = models.BooleanField()
    date_of_birth = models.DateField(null=False)
    occupation = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, null=False, unique=True)
    cpf = models.CharField(null=False, max_length=50)
    state = models.ForeignKey("States", null=False, on_delete=models.PROTECT)
    cep = models.CharField(null=False, max_length=50)
