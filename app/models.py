# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

provincesMap = {}
provincesMap[7] = "La Habana"
provincesMap[74] = "La Habana"
provincesMap[48] = "Pinar del Rio"
provincesMap[47] = "Artemisa/Mayabeque"
provincesMap[46] = "La Isla"
provincesMap[45] = "Matanzas"
provincesMap[43] = "Cienfuegos"
provincesMap[42] = "Villa Clara"
provincesMap[41] = "Sancti Spiritus"
provincesMap[33] = "Ciego de Avila"
provincesMap[32] = "Camaguey"
provincesMap[31] = "Las Tunas"
provincesMap[24] = "Holguin"
provincesMap[23] = "Granma"
provincesMap[22] = "Santiago de Cuba"
provincesMap[21] = "Guantanamo"


def province_str(num):
    return provincesMap[int(num)]

class AndroidMetadata(models.Model):
    locale = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'android_metadata'


class Fix(models.Model):
    model = 'Fix'
    number = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fix'

    def province_str(self):
        return province_str(self.province)

    def __str__(self):
        return '(%s :: %s :: %s)' %(self.number, self.name, self.province_str())


class Movil(models.Model):
    model = 'Movil'
    number = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    identification = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movil'

    def province_str(self):
        return province_str(self.province)

    def __str__(self):
        return '(%s :: %s :: %s)' %(self.number, self.name, self.province_str())


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'


class Version(models.Model):
    version = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version'
