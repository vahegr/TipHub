from django.db import models


class About(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    text = models.TextField(max_length=700, verbose_name='متن')
    allowing = models.BooleanField(default=False, verbose_name='مجاز')

    class Meta:
        verbose_name = 'درباره'
        verbose_name_plural = 'درباره ما'

    def __str__(self):
        return f"{self.title} - {self.text[:30]} ..."
