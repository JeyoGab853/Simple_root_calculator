from Equation_Organizer import organize_equation
from Equation_Organizer import EquationClass
from decimal import Decimal

import cmath
import math

# class FractionType():
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#
#     def show_fraction(self):
#         return f'{self.numerator}/{self.denominator}'

def find_divisors(number):
    rootTab = []

    for x in range(abs(number)):
        x = x + 1

        if abs(number) % x == 0:
            rootTab.append(x)
            rootTab.append(-x)

    return rootTab

def find_lcd(val1,val2):
    val1 = abs(val1)
    val2 = abs(val2)

    largestVal = max(val1,val2)

    for x in range(largestVal):
        if x <= 1:
            continue

        if val1 % x == 0 and val2 % x == 0:
            return x

    return 1

def to_fraction(divident,divisor):

    LCD = find_lcd(divident,divisor)

    numerator = int(abs(divident /LCD))
    denominator = int(abs(divisor / LCD))

    sign = divident/divisor

    if sign < 0:
        sign = '-'
    else:
        sign = ''

    if denominator == 1:
        return sign + str(numerator)

    stringFraction = str(numerator) + "/" + str(denominator)

    return sign + stringFraction

def all_possible_roots(equation: EquationClass) -> tuple[list,list]:
    constant = equation.constantTerm()
    leadingCoefficient = equation.leadingTerm().Coefficient

    p = find_divisors(constant)
    q = find_divisors(leadingCoefficient)

    rootList = []
    fractionedList = []

    for pVal in p:
        for qVal in q:
            root = Decimal(str(pVal))/Decimal(str(qVal))
            fractionedRoot = to_fraction(pVal,qVal)

            if not root in rootList:
                rootList.append(root)
                fractionedList.append(fractionedRoot)

    return rootList, fractionedList

def solve_with_root_theorem(equation: EquationClass,root: int | float): # won't work with multiple variables
    values = []

    for term in equation.Terms:
        degree = term.get_degree()

        evaluatedValue = Decimal(str(term.Coefficient)) * Decimal(str(root)) ** Decimal(str(degree))
        values.append(evaluatedValue)

    currentNumber = 0

    for v in values:
        currentNumber = Decimal(str(currentNumber)) + v

    if sum(values) == 0:
        return True

def sign(x):
    return (x > 0) - (x < 0)


def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("The coefficient 'a' cannot be zero.")

    # Calculate the discriminant (d = b^2 - 4ac)
    discriminant = (b ** 2) - (4 * a * c)

    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return root1, root2

def RootTheorem(equation: str):
    equation : EquationClass = organize_equation(equation)

    if type(equation) == str or len(equation.Terms) == 0:
        return equation

    if not equation:
        return "None"

    if equation.equationDegree() == 0:
        return "None"

    rootList, fractionedList = all_possible_roots(equation)

    zeroesList = []

    for i in range(len(rootList)):
        if solve_with_root_theorem(equation,rootList[i]):
            zeroesList.append(fractionedList[i])


    if len(zeroesList) < equation.equationDegree():
        return "Cannot Find"

    return zeroesList






