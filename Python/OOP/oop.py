# Create one class called FruitShop. 
# This class should receive a name which should be a string, and fruits as a list. 
# Create also a method called get_fruits_count() which should return amount of fruits in the shop.
# Input:my_shop = FruitShop("My Fruit Shop", ["Banana" , "Orange", "Kiwi","Apple"])
# Output: 4

'''
class FruitShop:
    def __init__(self, name, fruits):
        self.name = name
        self.fruits = fruits

    def get_fruits_count(self):
        return len(self.fruits)

my_shop = FruitShop("My Fruit Shop", ["Banana" , "Orange", "Kiwi","Apple"])
print(my_shop.get_fruits_count())
'''

# Create the following classes: Animal, Horse and Dog.
# The Animal class should have a method eat ( ) and it should return "eating.. nom.. nom.."
# The Horse class should have a method called neigh ( ) and it should return "neigh! 
# "The Dog class should have a method called bark ( ) and it should return "voof voof!"
# And remember that the Horse and Dog class should inherit form the Animal class.

'''
class Animal:
    def eat(self):
        return "eating.. nom.. nom.."

class Horse(Animal):
    def neigh(self):
        return "neigh!"

class Dog(Animal):
    def bark(self):
        return "voof voof!"

print(Animal().eat())
print(Horse().neigh())
print(Dog().bark())
'''

# Create the following classes: Person, Staff, Busdriver
# Person should have one method named walk( ) that should return "walking"
# Staff should have one method called work( ) that should return "working"
# Busdrivershould have one method called driving ( ) that returns "diving the bus"
# The Busdriver class should inherit from both Person and Staff 

'''
class Person:
    def walk(self):
        return "walking"

class Staff:
    def work(self):
        return "working"

class Busdriver(Person, Staff):
    def driving(self):
        return "diving the bus"

print(Person().walk())
print(Staff().work())
print(Busdriver().driving())
'''

# In this lab you have one person in a band that wants to play some instruments.
# Create one function and name it play_instrument( ) which will receive an instance of an instrument and will print its play () method.
# Note: You need to create separate files for each class as well.
import drums
import synth

def play_instrument(instrument):
    instrument.play()

synth = synth.Synth()
drums = drums.Drums()

play_instrument(drums)
play_instrument(synth)