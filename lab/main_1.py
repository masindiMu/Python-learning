import utilities


def main():
    """Main function to call utilities functions and display results."""
    # Circle Area
    radius_circle = float(input("Enter the radius of the circle: "))
    circle_area = utilities.calculate_circle_area(radius_circle)
    print(f"Circle Area: {circle_area:}")

    # Sphere Volume
    radius_sphere = float(input("Enter the radius of the sphere: "))
    sphere_volume = utilities.calculate_sphere_volume(radius_sphere)
    print(f"Sphere Volume: {sphere_volume:}")

    # BMI
    bmi = utilities.calculate_BMI()
    print(f"Your BMI: {bmi:}")

    # Hypotenuse
    hypotenuse = utilities.calculate_hypotenuse()
    print(f"Hypotenuse: {hypotenuse:}")


if __name__ == "__main__":
    main()