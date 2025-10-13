class cars:
    def __init__(self, brand, name, colour):
        self.brand = brand
        self.name = name
        self.colour = colour

    def describe(self):
        print("This is a " + self.brand + " which has a name " + self.name)
        print("This one is " + self.colour)

    def change_colour(self, new_colour):
        self.colour = new_colour

BMW = cars("BMW", "M3", "yellow")
Lambo = cars("Lambourghini", "Diabolo", "pink")

list_of_cars = [BMW, Lambo]
list_of_cars[0].brand

BMW.describe()

new_colour = input("Choose a colour: ")
BMW.change_colour(new_colour)

BMW.describe()