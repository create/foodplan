from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class FoodplanUser(AbstractBaseUser):

    email = models.EmailField(max_length=255, unique=True)
    birthdate = models.DateField()
    gender = models.BinaryField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birthdate', 'gender']


class FoodplanUserManager(BaseUserManager):

    def create_user(self, email, birthdate, gender, password=None):
        user = self.model(email=FoodplanUserManager.normalize_email(email), birthdate=birthdate, gender=gender)

        user.set_password(password)
        user.save(using=self._db)
        return user
