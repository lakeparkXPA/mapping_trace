# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Concept(models.Model):
    concept_id = models.IntegerField()
    concept_name = models.CharField(max_length=255)
    domain_id = models.CharField(max_length=20)
    vocabulary_id = models.CharField(max_length=20)
    concept_class_id = models.CharField(max_length=20)
    standard_concept = models.CharField(max_length=1, blank=True, null=True)
    concept_code = models.CharField(max_length=50)
    valid_start_date = models.DateField()
    valid_end_date = models.DateField()
    invalid_reason = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'concept'


class Domain(models.Model):
    domain_id = models.CharField(max_length=20)
    domain_name = models.CharField(max_length=255)
    domain_concept_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'domain'


class Local(models.Model):
    local_id = models.IntegerField(primary_key=True)
    local_code = models.CharField(max_length=50, blank=True, null=True)
    local_name = models.TextField(blank=True, null=True)
    local_name_kr = models.TextField(blank=True, null=True)
    edi = models.CharField(db_column='EDI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    local_site = models.CharField(max_length=10, blank=True, null=True)
    local_start_date = models.DateField(blank=True, null=True)
    local_end_date = models.DateField(blank=True, null=True)
    local_field = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local'


class Map(models.Model):
    map_id = models.IntegerField(primary_key=True)
    local_id = models.IntegerField()
    concept_id = models.IntegerField()
    vocabulary_id = models.CharField(max_length=20)
    map_person = models.CharField(max_length=100, blank=True, null=True)
    map_date = models.DateField(blank=True, null=True)
    map_current = models.CharField(max_length=1, blank=True, null=True)
    map_valid = models.CharField(max_length=1, blank=True, null=True)
    map_comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map'


class Temp(models.Model):
    atc = models.TextField(db_column='ATC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temp'


class Vocabulary(models.Model):
    vocabulary_id = models.CharField(max_length=20)
    vocabulary_name = models.CharField(max_length=255)
    vocabulary_reference = models.CharField(max_length=255, blank=True, null=True)
    vocabulary_version = models.CharField(max_length=255, blank=True, null=True)
    vocabulary_concept_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vocabulary'
