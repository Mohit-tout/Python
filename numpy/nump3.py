import numpy as py
from sympy import symbols, diff

x = symbols('x')
f = x**2
derivative = diff(f, x)
print("Derivative of x^2:", derivative)