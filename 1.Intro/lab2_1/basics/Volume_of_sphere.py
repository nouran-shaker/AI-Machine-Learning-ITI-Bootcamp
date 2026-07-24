#Program to take radius of a sphere and calculate its volume

from math import pi

radius = float(input("Enter the radius of the sphere: "))
volume = (4/3) * pi * radius**3
print("The volume of the sphere is: %.2f" % volume)
