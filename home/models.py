from django.db import models


class ContactInfo(models.Model):
    location = models.CharField(max_length=200, verbose_name='آدرس')
    support = models.CharField(max_length=15, verbose_name='پشتیبانی')
    email = models.EmailField(max_length=250, verbose_name='آدرس ایمیل')
    instagram = models.URLField(blank=True, verbose_name='آیدی اینستاگرام')
    telegram = models.URLField(blank=True, verbose_name='آدرس تلگرام')
    whatsapp = models.URLField(blank=True, verbose_name='آدرس واتساپ')
    twitter = models.URLField(blank=True, verbose_name='آدرس تویتر')
    allowing = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'اطلاعات تماس'
        verbose_name_plural = 'اطلاعات تماس'

    def __str__(self):
        return self.email
