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
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'

    def __str__(self):
        return self.username

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


class UserFollowing(models.Model):
    user = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE, verbose_name='کاربر')
    following_user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE, verbose_name='کابر دنبال کننده')
    its_following = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} followed {self.following_user} "

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'دنبال کننده'
        verbose_name_plural = 'دنبال کنندگان'
