# Create an abstract class Shape with abstract methods calculate_area and calculate_perimeter
# Create classes Circle (receives radius upon initialization) and 
# Rectangle (receives height and width upon initialization) that implement those methods (returning the result)
import Shape
import 

class Circle:
    def __init__(self, radius):
        self.radius = radius

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())