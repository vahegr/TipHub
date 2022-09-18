# Generated by Django 4.1 on 2022-09-17 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('text', models.TextField(max_length=700, verbose_name='متن')),
                ('allowing', models.BooleanField(default=False, verbose_name='مجاز')),
            ],
            options={
                'verbose_name': 'درباره',
                'verbose_name_plural': 'درباره ما',
            },
        ),
    ]