# Vehicle class
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    # Method to update the owner of the vehicle
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"The owner of vehicle {self.registration_number} has been updated to {self.owner}.")

# Creating instances of Vehicle
vehicle1 = Vehicle("ABC123", "Car", "John Deer")
vehicle2 = Vehicle("XYZ789", "Truck", "Alice Smith")


print(f"Initial owner of vehicle 1: {vehicle1.owner}")
vehicle1.update_owner("Jackie Garret")  # Updating owner of vehicle1

print(f"Initial owner of vehicle 2: {vehicle2.owner}")
vehicle2.update_owner("Josh Dunham")  # Updating owner of vehicle2
