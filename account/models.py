from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, felhasznalonev, password=None):
        if not email:
            raise ValueError("A felhasnálónak szüksége van email címre")
        if not felhasznalonev:
            raise ValueError("A felhasználónak szüksége van felhasználónévre")
        
        user = self.model(
            email=self.normalize_email(email),
            felhasznalonev=felhasznalonev,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, felhasznalonev, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            felhasznalonev=felhasznalonev,
        )

        user.admin = True
        user.feltolto = True
        user.foadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email                   =models.EmailField(verbose_name="email",max_length=60, unique=True)
    felhasznalonev          =models.CharField(max_length=30, unique=True)
    admin                   =models.BooleanField(default=False)
    feltolto                =models.BooleanField(default=False)
    foadmin                 =models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['felhasznalonev',]

    objects=MyAccountManager()

    def __str__(self):
        return self.email
    
    @property
    def is_staff(self):
        return self.feltolto

    def has_perm(self, perm, obj=None):
        return self.admin
    
    def has_module_perms(self, app_label):
        return True
    

