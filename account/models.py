from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='آدرس ایمیل',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=50,
        unique=True,
        default=['email'],
        verbose_name='نام کاربری'
    )
    full_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='نام و نام خانوادگی'
    )
    phone = models.CharField(
        max_length=12,
        unique=True,
        blank=True,
        null=True,
        verbose_name='شماره مبایل'
    )
    image = models.ImageField(
        upload_to='images/users',
        null=True,
        blank=True,
        verbose_name='تصویر کاربر'
    )
    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name='درباره'
    )
    instagram = models.URLField(
        blank=True,
        null=True,
        unique=True,
        verbose_name='آیدی اینستاگرام'
    )
    github = models.URLField(
        blank=True,
        null=True,
        unique=True,
        verbose_name='آدرس گیتهاب'
    )
    linkedin = models.URLField(
        blank=True,
        null=True,
        unique=True,
        verbose_name='آدرس لینکدین'
    )
    twitter = models.URLField(
        blank=True,
        null=True,
        unique=True,
        verbose_name='آدرس توییتر'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='فعالیت'
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name='ادمین'
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        " Is the user a member of staff? "
        # Simplest possible answer: All admins are staff
        return self.is_admin
