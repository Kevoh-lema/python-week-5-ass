# Base class representing a Superhero
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
        self._secret_identity = "Unknown"  # This is a protected variable (we won't allow direct access)

    def reveal_identity(self):
        return f"{self.name} is secretly {self._secret_identity}."

    def use_power(self):
        print(f"{self.name} uses {self.power} to save {self.city}!")

    def set_secret_identity(self, identity):
        self._secret_identity = identity

# Derived class representing a Flying Superhero
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)  # Initialize the base class attributes
        self.flight_speed = flight_speed

    def use_power(self):
        # Overriding the base class method to include flying ability
        super().use_power()
        print(f"{self.name} flies at {self.flight_speed} mph to the rescue!")

# Create instances of the Superhero and FlyingHero classes
hero = Superhero("Captain Justice", "Super Strength", "Metropolis")
flying_hero = FlyingHero("Sky Swift", "Flight", "Gotham", 500)

# Using the methods
print(hero.reveal_identity())  # Identity info
hero.use_power()  # Using superhero's power

print(flying_hero.reveal_identity())  # Identity info for flying hero
flying_hero.use_power()  # Using flying hero's power
