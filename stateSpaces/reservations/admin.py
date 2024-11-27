from django.contrib import admin

from .models import(Agent, AgentBuilding, Amenity, AmenityVenue, 
                    AvailableVenue, Building, Customer, MemberAssignment,
                    Reservation, UnavailableVenue, Venue, VenueBuilding
) 

class AgentBuildingInLine(admin.StackedInline):
    model = AgentBuilding

class VenueBuildingInLine(admin.StackedInline):
    model = VenueBuilding

class AmenityVenueInLine(admin.StackedInline):
    model = AmenityVenue

class MemberAssignmentInLine(admin.StackedInline):
    model = MemberAssignment

class ReservationInline(admin.StackedInline):
    model = Reservation

class AVInline(admin.StackedInline):
    model = AvailableVenue


class AgentAdmin(admin.ModelAdmin):
    model = Agent
    inlines = [AgentBuildingInLine, MemberAssignmentInLine, ]

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    inlines = [ReservationInline, ]

class AmenityAdmin(admin.ModelAdmin):
    model = Amenity
    inlines = [AmenityVenueInLine,]

class BuildingAdmin(admin.ModelAdmin):
    model = Building
    inlines = [AgentBuildingInLine, VenueBuildingInLine, ]

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation


class VenueAdmin(admin.ModelAdmin):
    model = Venue
    inlines = [AVInline, AmenityVenueInLine,  VenueBuildingInLine, ReservationInline, ]

class AvailableVenueAdmin(admin.ModelAdmin):
    model = AvailableVenue

class UnavailableVenueAdmin(admin.ModelAdmin):
    model = UnavailableVenue

admin.site.register(Agent, AgentAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(AvailableVenue, AvailableVenueAdmin)
admin.site.register(UnavailableVenue, UnavailableVenueAdmin)

