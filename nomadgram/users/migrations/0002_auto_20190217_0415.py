# Generated by Django 2.0.13 on 2019-02-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('not-specified', 'Not sepecified')], max_length=80, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=50, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='user',
            name='website',
            field=models.URLField(null=True, verbose_name=''),
        ),
    ]
