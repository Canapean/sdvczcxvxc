import django.contrib.auth.models
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to=django.contrib.auth.models.User,
        on_delete=models.CASCADE
    )
    is_status = models.BooleanField(
        default=True,
        choices=(
            (False, 'User'),
            (True, 'Admin')
        )
    )
