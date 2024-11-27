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
    agent = models.OneToOneField(Agent, models.DO_NOTHING, primary_key=True)
    building = models.ForeignKey('Building', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'agentbuilding'


class Amenity(models.Model):
    amenity_id = models.CharField(primary_key=True, max_length=5)
    amenity_type = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'amenity'


class Amenityvenue(models.Model):
    amenity = models.OneToOneField(Amenity, models.DO_NOTHING, primary_key=True)
    venue = models.ForeignKey('Venue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'amenityvenue'


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


class Memberassignment(models.Model):
    member_name = models.CharField(primary_key=True, max_length=255)
    agent = models.ForeignKey(Agent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'memberassignment'


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
