# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Concept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Domain(models.Model):
    domain_id = models.CharField(primary_key=True, max_length=20)
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
    vocabulary_id = models.CharField(primary_key=True, max_length=20)
    vocabulary_name = models.CharField(max_length=255)
    vocabulary_reference = models.CharField(max_length=255, blank=True, null=True)
    vocabulary_version = models.CharField(max_length=255, blank=True, null=True)
    vocabulary_concept_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vocabulary'
