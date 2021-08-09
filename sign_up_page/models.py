from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyAccountManager(BaseUserManager):

    def create_user(self, fullname, username, dob, gender, email, state, city, pincode, password):
        if not username:
            raise ValueError("User must have an username.")
        user = self.model(
            fullname = fullname,
            username = username,
            dob = dob,
            gender = gender,
            email = self.normalize_email(email),
            state = state,
            city = city,
            pincode = pincode,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, fullname, username, dob, gender, email, state, city, pincode, password):
        user = self.create_user(
            fullname = fullname,
            username = username,
            dob = dob,
            gender = gender,
            email = self.normalize_email(email),
            state = state,
            city = city,
            pincode = pincode,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.
class Account(AbstractBaseUser):
    fullname        = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique =True)
    dob             = models.DateField(verbose_name="dob")
    gender          = models.CharField(max_length=10)
    email           = models.EmailField(verbose_name="email", max_length=50, unique = True)
    state           = models.CharField(max_length=50)
    city            = models.CharField(max_length=50)
    pincode         = models.IntegerField()
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    date_joined     = models.DateTimeField(verbose_name="date joined", auto_now_add=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fullname','dob','gender','email','state','city','pincode']

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True