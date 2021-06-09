from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(username, email, password, **other_fields)

    def create_user(self, username, email, password=None, **other_fields):
        if not username:
            raise ValueError("Username address is mandatory")
        if not email:
            raise ValueError("Email address is mandatory")
        if not password:
            raise ValueError("Password is mandatory")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, username, email, password):

        user = self.create_user(
            username,
            password=password,
            email=self.normalize_email(email)
        )

        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class ProfileManager(BaseUserManager):
    def create_profile(self, user, phoneno, registration_mode, company):
        if not user.username:
            raise ValueError("Username address is mandatory")
        if not user.email:
            raise ValueError("Email address is mandatory")
        if not user.password:
            raise ValueError("Password is mandatory")
        user_obj = self.model(
            email=self.normalize_email(user.email)
        )
        user_obj.set_password(user.password)

        user_obj.save(using=self._db)
        return user_obj


class User(AbstractBaseUser, PermissionsMixin):
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=50, unique=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_module_perms(self, app_label):
        return True

    # Create your models here.
    def has_perm(self, perm, obj=None):
        return True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CLIENT_CHOICES = (
        ('Guest User', 'Guest User'),
        ('Freelance Client', 'Freelance Client')
    )
    phoneno = PhoneField()
    registration_mode = models.CharField(choices=CLIENT_CHOICES, max_length=25)
    company = models.CharField(max_length=20)
    REQUIRED_FIELDS = ['user', 'phoneno', 'registration_mode', 'company']
    profileobjects = ProfileManager()

    def __str__(self):
        return self.user.username
