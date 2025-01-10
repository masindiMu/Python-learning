import math

def calculate_circle_area(radius):
    area = math.pi * radius **2
    return area


def calculate_sphere_volume(radius):
    volume = 4/3 *(math.pi * radius ** 3)
    return volume


def calculate_BMI():
    weight_kg = float(input("Weight in kilograms:"))
    height_m = float( input("height in meter:"))
    bmi = weight_kg / (height_m * height_m)
    return bmi


def calculate_hypotenuse():
    side_a = float( input("length of side A:"))
    side_b = float( input("length of side B:"))
    return math.hypot(side_a, side_b)

