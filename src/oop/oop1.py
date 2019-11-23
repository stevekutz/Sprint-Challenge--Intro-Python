# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle():   # my base class, Parent is Vehicle but no props/methods for child classes to inherit
    pass

# children of Vehicle  Vehicle -> GroundVehicle
class GroundVehicle(Vehicle):    
    pass

class FlightVehicle(Vehicle):
    pass


##########  children of GroundVehicle   ##########
# child of GroundVehicle    Vehicle -> GroundVehicle -> Car
class Car(GroundVehicle):
    pass

# child of GroundVehicle    Vehicle -> GroundVehicle -> Motorcycle
class Motorcycle(GroundVehicle):   
    pass
#################################################


##########  children of FlightVehicle   ##########
# child of FlightVehicle     Vehicle -> FlightVehicle -> Startship
class Starship(FlightVehicle):  
    pass

# child of FlightVehicle     Vehicle -> FlightVeichle -> Airplane
class Airplane(FlightVehicle):
    pass
#################################################