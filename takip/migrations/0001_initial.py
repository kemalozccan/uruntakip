# Generated by Django 4.2.3 on 2023-07-23 17:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UruntakipModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alıcı', models.CharField(max_length=120)),
                ('urun_modeli', models.CharField(max_length=50)),
                ('urun_kodu', models.CharField(max_length=12)),
                ('satis_tarihi', models.DateField()),
                ('alıcı_adresi', models.CharField(blank=True, max_length=175)),
                ('alıcı_tel', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('alıcı_mail', models.EmailField(max_length=254)),
            ],
        ),
    ]