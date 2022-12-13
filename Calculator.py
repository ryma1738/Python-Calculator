'''
Project Name: The Calculator
Author: Ryan Jepson
Todo: 1. add a save function, 2. add more equations

For information on how to use the program enter 0 as the first Argument
in the terminal
'''

import math
import fractions
import sys

error = "You did not enter a valid answer please try again.\n"


def info():
    """Opens the Info page in the terminal to show you how to use the program"""
    with open(r'info_calculator.txt', 'r') as F:
        for line in F:
            print(line)


# deffing all the difrent formulas with functions
def pythagorean_theorem():
    if len(sys.argv) > 1:
        a = float(sys.argv[3])
        b = float(sys.argv[4])
        c = float(sys.argv[5])
        solve = sys.argv[2].strip().upper()
    else:
        while True:
            print("You picked Pythagrean theorem: c^2 = a^2 + b^2")
            solve = input("Would you like to solve for A, B, or C? :")
            solve = solve.upper().strip()
            if solve == 'A' or solve == 'B' or solve == 'C':
                break
            else:
                print(error)
                continue
    if solve == "A":
        try:
            if len(sys.argv) == 1:
                print("You picked solve for A:")
                b = float(input("B = "))
                c = float(input("C = "))
            a = round(math.sqrt(c ** 2 - b ** 2), 2)
            print("The Answer is A =", a)
        except ValueError:
            print(error)
    elif solve == "B":
        try:
            if len(sys.argv) == 1:
                print("You picked solve for B:")
                a = float(input("A = "))
                c = float(input("C = "))
            b = round(math.sqrt(c ** 2 - a ** 2), 2)
            print("The Answer is B =", b)
        except ValueError:
            print(error)
    elif solve == "C":
        try:
            if len(sys.argv) == 1:
                print("You picked solve for C:")
                a = float(input("A = "))
                b = float(input("B = "))
            c = round(math.sqrt(a ** 2 + b ** 2), 2)
            print("The Answer is C =", c)
        except ValueError:
            print(error)


def area_shape():
    ''' This is a formula for determineing the varius shapes we may want to caluculate
    area for.
    '''
    if len(sys.argv) > 1:
        if sys.argv[2] == '1':
            area_triangle()
        elif sys.argv[2] == '2':
            area_rectangle()
        elif sys.argv[2] == '3':
            area_circle()
        elif sys.argv[2] == '4':
            area_cylinder()
    else:
        while True:
            print(f"Which shape would you like to calculate (Please Capitalize):")
            print("\n 1: Triangle\n 2: Rectangle\n 3: Circle\n 4: Cylinder\n ")
            shape = input("Shape: ")
            shape = shape.strip()
            if shape == "1":
                area_triangle()
                break
            elif shape == "2":
                area_rectangle()
                break
            elif shape == "3":
                area_circle()
                break
            elif shape == '4':
                area_cylinder()
                break
            else:
                print(error)
                continue


def area_rectangle():
    if len(sys.argv) > 1:
        L = float(sys.argv[3])
        W = float(sys.argv[4])
    else:
        print("You picked the area of a rectangle: A = L * W")
        L = float(input("Length of rectangle: "))
        W = float(input("Width of rectangle: "))
    A = round(L * W, 3)
    print("The Area of the Rectangle is:", A)


def area_triangle():
    if len(sys.argv) > 1:
        H = float(sys.argv[3])
        B = float(sys.argv[4])
    else:
        print("You picked the area of a triangle: A = (H * B) / 2")
        H = float(input("Height of triangle: "))
        B = float(input("Base of triangle: "))
    A = (H * B) / 2
    print("The area of the triangle is:", A)


def area_circle():
    if len(sys.argv) > 1:
        radius = float(sys.argv[3])
    else:
        print("You picked area of a circle: A = (pi) * r^2")
        radius = float(input("Radius = "))
    answer = round(math.pi * (radius ** 2), 2)
    print("The area of the circle is:", answer)


def area_cylinder():
    if len(sys.argv) > 1:
        radius = float(sys.argv[3])
        height = float(sys.argv[4])
    else:
        print('You picked the area of a cylinder A = (2*(pi)*R*H) + (2*(pi)*r^2)')
        radius = float(input('Radius = '))
        height = float(input('Height = '))
    answer = round((2 * math.pi * radius * height) + (2 * math.pi * radius ** 2), 2)
    print(f"The area of the cylinder is {answer}")


def quadratic_formula():
    if len(sys.argv) > 1:
        A = float(sys.argv[2])
        B = float(sys.argv[3])
        C = float(sys.argv[4])
    else:
        print('You picked the quadratic formula: x=(-b +or- sqrt(b^2 - 4*A*C) / 2*A')
        A = int(input("A = "))
        B = int(input("B = "))
        C = int(input("C = "))
    while True:
        y_n = input("Can the answer have a decimal? Yes (Y) or No (N): ")
        y_n = y_n.strip().upper()
        if y_n == "Y" or y_n == '':
            try:
                part_one = math.sqrt(B ** 2 - 4 * A * C)
                answer_one = (B * -1) + part_one
                answer_two = (B * -1) - part_one
                answer_one = round(answer_one / (2 * A), 2)
                answer_two = round(answer_two / (2 * A), 2)
                print('\nThe answer is', answer_one, +answer_two)
                break
            except ValueError:
                print('\nTheir is no real solution.')
                break
        elif y_n == "N":
            try:
                part_one = B ** 2 - 4 * A * C

                if part_one > 0:
                    part_one_s = math.sqrt(part_one)
                    answer_one = (B * -1) + part_one_s
                    answer_two = (B * -1) - part_one_s
                    answer_one = answer_one / (2 * A)
                    answer_two = answer_two / (2 * A)
                    answer_one = fractions.Fraction(answer_one)
                    answer_two = fractions.Fraction(answer_two)
                    print("\nThe answer is", answer_one, ",", +answer_two)
                    break
                else:
                    b = (B * -1)
                    bottom = 2 * A
                    print("The answer is\n", b, "+sqrt(", +part_one, ") /", +bottom, ",\n", +b, "-sqrt(", +part_one,
                          ") /", +bottom)
                    break
            except ValueError:
                print('\nTheir is no solution.')
                break
        else:
            print(error)
            continue


def factoring():
    pass


def main(argv):
    '''
    This is the main function were all the code is executed. This makes the
    code cleaner and run better. If the program is not run with arguments from the
    terminal, it starts a while loop to allow you to solve multiple equations.
    Otherwise it only runs one operation. Using system arguments is much faster.
    '''
    if len(sys.argv) > 1:
        if argv[1] == '0':
            info()
        elif argv[1] == '1':
            pythagorean_theorem()
        elif argv[1] == '2':
            area_shape()
        elif argv[1] == '3':
            quadratic_formula()
    else:
        print("Welcome to the calculator! Pease enter the number of the function you would like to execute. \n")
        # deffinging the valuesfor the while loop
        end_program = "null"
        while end_program != "end":
            print(
                "Pick a number from one of the folowing:\n 1: Pythagorean Theorem\n 2: Area of a shape\n 3: Quadratic Formula\n")
            formula = input("Your choice: ")
            formula = formula.strip()
            if formula == "1":
                pythagorean_theorem()

            elif formula == "2":
                area_shape()

            elif formula == "3":
                quadratic_formula()

            else:
                print("Your answer did not match any of the options please try again.\n")
                continue

            end_program = input("\nWould you like to do another calculation? If not type end: ")
            end_program = end_program.strip().lower()

        print("\n Thank you for using The Calculator!")


if __name__ == "__main__":  # this makes the program use a main function
    main(sys.argv)
