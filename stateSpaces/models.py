# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agent(models.Model):
    agent_id = models.CharField(primary_key=True, max_length=5)
    agent_first_name = models.CharField(max_length=255)
    agent_last_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'agent'


class Agentbuilding(models.Model):
    agent = models.OneToOneField(Agent, models.DO_NOTHING, primary_key=True)  # The composite primary key (agent_id, building_id) found, that is not supported. The first column is selected.
    building = models.ForeignKey('Building', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'agentbuilding'
        unique_together = (('agent', 'building'),)


class Amenity(models.Model):
    amenity_id = models.CharField(primary_key=True, max_length=5)
    amenity_type = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'amenity'


class Amenityvenue(models.Model):
    amenity = models.OneToOneField(Amenity, models.DO_NOTHING, primary_key=True)  # The composite primary key (amenity_id, venue_id) found, that is not supported. The first column is selected.
    venue = models.ForeignKey('Venue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'amenityvenue'
        unique_together = (('amenity', 'venue'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Availablevenue(models.Model):
    a_venue = models.OneToOneField('Venue', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'availablevenue'


class Building(models.Model):
    building_id = models.CharField(primary_key=True, max_length=5)
    building_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'building'


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=5)
    customer_first_name = models.CharField(max_length=255, blank=True, null=True)
    customer_middle_initial = models.CharField(max_length=2, blank=True, null=True)
    customer_last_name = models.CharField(max_length=255)
    birth_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'customer'


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
    id = models.BigAutoField(primary_key=True)
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


class Memberassignment(models.Model):
    agent = models.OneToOneField(Agent, models.DO_NOTHING, primary_key=True)  # The composite primary key (agent_id, member_name) found, that is not supported. The first column is selected.
    member_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'memberassignment'
        unique_together = (('agent', 'member_name'),)


class Reservation(models.Model):
    reservation_id = models.CharField(primary_key=True, max_length=5)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    venue = models.ForeignKey('Venue', models.DO_NOTHING)
    number_of_participants = models.IntegerField()
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'reservation'


class Unavailablevenue(models.Model):
    u_venue = models.OneToOneField('Venue', models.DO_NOTHING, primary_key=True)
    renovation_date_start = models.DateField()
    renovation_date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'unavailablevenue'


class Venue(models.Model):
    venue_id = models.CharField(primary_key=True, max_length=5)
    venue_name = models.CharField(max_length=255)
    floor_area = models.IntegerField()
    capacity = models.IntegerField()
    venue_type = models.CharField(max_length=255)
    floor = models.IntegerField()
    under_renovation = models.BooleanField(blank=True, null=True)
    reservation_fee = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'venue'


class Venuebuilding(models.Model):
    venue = models.OneToOneField(Venue, models.DO_NOTHING, primary_key=True)
    building = models.ForeignKey(Building, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'venuebuilding'
