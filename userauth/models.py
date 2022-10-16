from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):

    def create_user(self, name, username, email, password):
        if not username:
            raise ValueError("User must have an username.")
        user = self.model(
            name = name,
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, username, email, password):
        user = self.create_user(
            name = name,
            username = username,
            email = email,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.
class Account(AbstractBaseUser):
    name            = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique =True)
    email           = models.EmailField(max_length=50, unique =True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True