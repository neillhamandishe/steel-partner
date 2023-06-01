from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=25, unique=True)

    def __str__(self):
        return f"{self.email if self.email else self.phone}"
