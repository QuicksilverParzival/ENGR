import math
r = 3
h = 4
surface_area = (math.pi * r ** 2) + (math.pi * r * math.sqrt(r**2 + h ** 2))
print("Given a radius of ", r, "[cm] and a height of ", h, "[cm],")
print("the surface area of a cone is ", surface_area, "[cm^3]")