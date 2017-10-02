#step#1
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year,color):
        """Initialize attributes of the parent class."""
        self.color = color
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016,'blue')
print(my_tesla.get_descriptive_name())
print(my_tesla.color)

class point():
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, x, y,):
        self.x=x
        self.y=y
        """Initialize attributes of the parent class."""

class shape():
    def __init__(self,area):
        self.area=area

    def draw(self):
        print("Drwaing")

class rectangle(shape):
    def __init__(self,top_left,bottom_right,area):
        super().__init__(area)
        self.top_left=top_left
        self.bottom=bottom_right

    def draw(self):
        print("Drawing Rectangle")

draw_rect = rectangle(4,5,20)
draw_rect.draw()

#ISA  parent child ISA relation
#HasA composition has a relation 
