from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CUSTOMER = 1
    DRIVER = 2
    ROLES = (
        (CUSTOMER, 'customer'),
        (DRIVER, 'driver')
    )

    role = models.SmallIntegerField(choices=ROLES, default=CUSTOMER)

    def __str__(self):
        return self.username
