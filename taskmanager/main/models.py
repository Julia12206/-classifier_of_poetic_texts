# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TextsModel(models.Model):

    klaccName = models.TextField(db_column='klaccName', unique=True)

    klacc = models.AutoField(db_column='klaccID', primary_key=True)

    class Meta:
        managed = True
        db_table = 'texts_klasses'

    def __str__(self):
        return str(self.klacc)


class Texts(models.Model):

    itemID = models.AutoField(db_column='itemID', primary_key=True)
    klacc = models.ForeignKey(TextsModel, models.DO_NOTHING, db_column='klaccID')
    #klaccName = models.ForeignKey(TextsModel,models.DO_NOTHING, db_column='klaccNmame')
    klaccName = models.TextField(db_column='klaccNmame', unique=True)
    author = models.TextField(db_column='author', unique=True)
    nazvanie = models.TextField(db_column='nazvanie', unique=True)
    stih = models.TextField(db_column='stih', unique=True)



    class Meta:
        managed = True
        db_table = 'texts'

    def __str__(self):
        return str(self.nazvanie)


