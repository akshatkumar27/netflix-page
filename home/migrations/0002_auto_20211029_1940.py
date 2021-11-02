# Generated by Django 3.2.7 on 2021-10-29 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderform',
            name='Email',
            field=models.EmailField(default='abc@gmailo.com', max_length=254),
        ),
        migrations.AddField(
            model_name='orderform',
            name='Password',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]