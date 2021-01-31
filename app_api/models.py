from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """manager for user profile"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('User must have an email address to proceed')

        """normalize the email"""

        email = self.normalize_email(email)
        """creating our user model"""
        user = self.model(email=email, name=name)

        """setting password"""
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create and save the new super user"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        """is_superuser is created automatically by the permissionsmxin"""
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    """to manage users with django"""
    objects = UserProfileManager()

    """work with django admin and authentication system """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    """giving django the full ability to get full name and to intract with our custom user model """

    def get_full_name(self):
         """retrive full name of user"""
         return self.name

    def get_short_name(self):
        """Retrieve short name"""
        return self.name

        """recommende for all django models"""
    def __str__(self):
        """Return string representation of out user"""
        return self.email
