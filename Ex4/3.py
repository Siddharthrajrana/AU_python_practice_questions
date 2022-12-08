def area_sphere(radius):
    return 3.14*radius**2

def vol_sphere(rad):
    return (4/3)*(3.14)*(rad**3)

radius=float(input("Enter the radius of the Sphere : "))
print("Area = ",format(area_sphere(radius)))
print("Volume =",format(vol_sphere(radius)))
