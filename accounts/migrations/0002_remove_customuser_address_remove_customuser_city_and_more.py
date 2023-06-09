# Generated by Django 4.2.1 on 2023-06-08 07:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='state',
        ),
        migrations.AddField(
            model_name='shopperprofile',
            name='address',
            field=models.CharField(default='bodija', max_length=255, verbose_name='address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopperprofile',
            name='city',
            field=models.CharField(default='ibadan', max_length=30, verbose_name='city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopperprofile',
            name='date_cerated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='shopperprofile',
            name='firstname',
            field=models.CharField(default='my profile', max_length=30, verbose_name='first name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopperprofile',
            name='lastname',
            field=models.CharField(default='kal', max_length=30, verbose_name='last name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopperprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='phone number'),
        ),
        migrations.AddField(
            model_name='shopperprofile',
            name='state',
            field=models.CharField(default='oyo', max_length=30, verbose_name='state'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='bodija', max_length=255, verbose_name='address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='ibadan', max_length=30, verbose_name='city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_cerated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstname',
            field=models.CharField(default='firstname', max_length=30, verbose_name='first name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastname',
            field=models.CharField(default='lastname', max_length=30, verbose_name='last name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='phone number'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.CharField(default='oyo', max_length=30, verbose_name='state'),
            preserve_default=False,
        ),
    ]
