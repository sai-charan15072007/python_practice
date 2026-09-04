# Example 1: Simple class with attributes and methods

class Car:
    def __init__(self, brand, model, year):
        """Constructor to initialize object attributes"""
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        """Method to display car details"""
        print(f"{self.year} {self.brand} {self.model}")

# Create objects (instances) of Car
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model 3", 2023)

# Call methods
car1.display_info()
car2.display_info()
