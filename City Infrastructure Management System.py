# Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. 
# This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.
# Task 1: Vehicle Registration System
# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner.
# Code Example: Provide a basic structure for the Vehicle class without methods.
    # class Vehicle:
        # def __init__(self, reg_num, type, owner):
            # self.registration_number = reg_num
            # self.type = type
            # self.owner = owner
# Expected Outcome: Completion of the Vehicle class with the update_ownermethod and a demonstration script showing the creation of Vehicle objects and updating their owners.


class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner  
        

Vehiclelist = []

Vehicle1 = Vehicle("1234", "Car", "John")
Vehicle2 = Vehicle("5678", "Bike", "Sam")
Vehicle3 = Vehicle("91011", "Truck", "Tom")

Vehiclelist.append(Vehicle1)
Vehiclelist.append(Vehicle2)
Vehiclelist.append(Vehicle3)

print("Before Update")
for i in Vehiclelist:
    print(i.registration_number, i.type, i.owner)
    
Vehicle1.update_owner("Mike")
Vehicle2.update_owner("David")
Vehicle3.update_owner("Harry")

print("\nAfter Update")
for i in Vehiclelist:
    print(i.registration_number, i.type, i.owner)
    

    
