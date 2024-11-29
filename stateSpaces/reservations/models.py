from django.db import models

# Create your models here.
from django.urls import reverse


class Agent(models.Model):
    agent_id = models.CharField(primary_key=True, max_length=5)
    agent_first_name = models.CharField(max_length=255)
    agent_last_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'agent'

    def __str__(self):
        return (self.agent_first_name+' '+self.agent_last_name)


class AgentBuilding(models.Model):
    agent = models.OneToOneField(Agent, models.DO_NOTHING, primary_key=True)
    building = models.ForeignKey('Building', models.DO_NOTHING, related_name='agentBuilding')

    class Meta:
        managed = False
        db_table = 'agentbuilding'

    def __str__(self):
        return str(self.agent)

class Amenity(models.Model):
    amenity_id = models.CharField(primary_key=True, max_length=5)
    amenity_type = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'amenity'
    
    def __str__(self):
        return self.amenity_type


class AmenityVenue(models.Model):
    amenity = models.OneToOneField(Amenity, models.DO_NOTHING, primary_key=True)
    venue = models.ForeignKey('Venue', models.DO_NOTHING, related_name='amenityVenue')

    class Meta:
        managed = False
        db_table = 'amenityvenue'

    def __str__(self):
        return str(self.amenity)

class AvailableVenue(models.Model):
    a_venue = models.OneToOneField('Venue', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'availablevenue'

    def __str__(self):
        return str(self.a_venue)

class Building(models.Model):
    building_id = models.CharField(primary_key=True, max_length=5)
    building_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'building'

    def __str__(self):
        return self.building_name
    
    def get_assigned_agent(self):
        agent_building = self.agentBuilding.first()
        return agent_building.agent

class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=5)
    customer_first_name = models.CharField(max_length=255, blank=True, null=True)
    customer_middle_initial = models.CharField(max_length=2, blank=True, null=True)
    customer_last_name = models.CharField(max_length=255)
    birth_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return (self.customer_last_name + ' ' + self.customer_first_name)

class MemberAssignment(models.Model):
    member_name = models.CharField(primary_key=True, max_length=255)
    agent = models.ForeignKey(Agent, models.DO_NOTHING, related_name='member')

    class Meta:
        managed = False
        db_table = 'memberassignment'

    def __str__(self):
        return self.member_name

class Reservation(models.Model):
    reservation_id = models.CharField(primary_key=True, max_length=5)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, related_name='reservation')
    venue = models.ForeignKey('Venue', models.DO_NOTHING, related_name='reserved')
    number_of_participants = models.IntegerField()
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'reservation'

    def __str__(self):
        return self.reservation_id

class UnavailableVenue(models.Model):
    u_venue = models.OneToOneField('Venue', models.DO_NOTHING, primary_key=True)
    renovation_date_start = models.DateField()
    renovation_date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'unavailablevenue'

    def __str__(self):
        return str(self.u_venue)

class Venue(models.Model):
    venue_id = models.CharField(primary_key=True, max_length=5)
    venue_name = models.CharField(max_length=255)
    floor_area = models.IntegerField()
    capacity = models.IntegerField()
    venue_type = models.CharField(max_length=255)
    floor = models.IntegerField()
    under_renovation = models.BooleanField(blank=False, null=True)
    reservation_fee = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'venue'

    def __str__(self):
        return self.venue_name

class VenueBuilding(models.Model):
    venue = models.OneToOneField(Venue, models.DO_NOTHING, primary_key=True)
    building = models.ForeignKey(Building, models.DO_NOTHING, related_name='venueBuilding')

    class Meta:
        managed = False
        db_table = 'venuebuilding'

    def __str__(self):
        return str(self.venue)