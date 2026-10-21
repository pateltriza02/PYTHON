from shapes.circle import area as circle_area
from shapes.circle import circumference
from shapes.rectangle import area as rectangle_area
from shapes.rectangle import perimeter

radius = 5

length = 10
width = 5

print("Circle area:", circle_area(radius))
print("Circle circumference:", circumference(radius))

print("Rectangle area:", rectangle_area(length, width))
print("Rectangle perimeter:", perimeter(length, width))
