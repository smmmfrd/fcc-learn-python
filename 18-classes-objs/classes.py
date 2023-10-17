class Vehicle:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")


my_car = Vehicle("Toyota", "Tacoma")

my_car.moves()
my_car.get_make_model()

your_car = Vehicle("Cadillac", "Escalade")

your_car.get_make_model()
your_car.moves()


# Inheritance
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id) -> None:
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along...")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")


class GolfCart(Vehicle):
    pass


cessna = Airplane("Cessna", "Skyhawk", "G3B1")
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaha", "GC100")

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()

print("\n\n")

# Polymorphism, same methods, different behavior
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
