from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class UruntakipModel(models.Model):
    alıcı = models.CharField(max_length=120, blank=False, null=False)
    urun_modeli = models.CharField(max_length=50,blank=False, null=False)
    urun_kodu = models.CharField(max_length=12, blank=False, null=False)
    satis_tarihi = models.DateField(auto_now=False, auto_now_add=False)
    alıcı_adresi = models.CharField(max_length=175, blank=True, null=False)
    alıcı_tel = PhoneNumberField()
    alıcı_mail = models.EmailField(blank=False, null=False)    



    class Meta:
        db_table='tablo_uruntakip'