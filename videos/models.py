import datetime
import jdatetime
from django.db import models
from django_jalali.db import models as jmodels
from django.utils import timezone
from extensions.utils import jalali_converter
from account.models import User
from django_extensions.db.fields import AutoSlugField
from django.utils.text import slugify


def slugify_function(content): return slugify(content, allow_unicode=True)


class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField()


class Category(models.Model):                                           # category of blogs
    parent = models.ForeignKey(
        'self',
        default=None,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='زیر دسته'
    )
    title = models.CharField(max_length=100, verbose_name='عنوان')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان تولید')
    slug = AutoSlugField(populate_from=['title'],
                         unique=True,
                         allow_unicode=True,
                         slugify_function=slugify_function,
                         blank=True,
                         verbose_name='اسلاگ'
                         )

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Video(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='تولید کننده ')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.TextField(max_length=600, verbose_name='شرح')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان تولید')
    jalali_created = jmodels.jDateField(auto_now_add=True, null=True, verbose_name='زمان تولید فارسی')
    jalali_updated = jmodels.jDateField(auto_now=True, null=True, verbose_name='به روز شده ')

    cover_image = models.ImageField(upload_to='images/video-images',
                                    null=True,
                                    verbose_name='تصویر کاور ویدیو',
                                    )
    video = models.FileField(upload_to='videos', null=True, verbose_name='ویدیو')
    allowing = models.BooleanField(default=False, verbose_name='مجاز')

    slug = AutoSlugField(populate_from=['title'],
                         unique=True,
                         allow_unicode=True,
                         slugify_function=slugify_function,
                         blank=True,
                         verbose_name='اسلاگ'
                         )

    hits = models.ManyToManyField(IpAddress,
                                  blank=True,
                                  related_name="hits",
                                  verbose_name='بازدید'
                                  )

    class Meta:
        verbose_name = 'ویدیو'
        verbose_name_plural = 'ویدیو ها'
        ordering = ('-created_at',)

    def jalali_date(self):
        return jalali_converter(str(self.jalali_created))

    def __str__(self):
        return f"{self.title} - {self.description[:30]} ... "
