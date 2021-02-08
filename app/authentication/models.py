from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    """ Manager for user profiles. Extends the base user manager """
    def create_user(self, email, password=None, **extra_fields):
        """ Creates and saves new user"""
        if not email:
            raise TypeError('Users must have a Email')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """ Creates and saves new superuser, it's created only from the console """
        if password is None:
            raise TypeError('Users must have a password')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google', 'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom database user model that support using email instead of username """
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    title = models.CharField(max_length=15,
                             choices=[('MR', 'Mr'), ('MS', 'Ms'), ('MISS', 'Miss'), ('MRS', 'Mrs')])

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    auth_provider = models.CharField(max_length=255, blank=False,
                                     null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email'] """ could be added date_of_birth i.e.  """

    objects = UserManager()

    def __str__(self):
        """ Return string representation of the user """
        return self.email

    def tokens(self):
        """ Return user token for active user """
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
