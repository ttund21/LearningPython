from math import sqrt

def eq2(a, b, c):
    delta = (b)**2 - 4 * a * c
    return ((-(b) + sqrt(delta)) / (2 * a)), ((-(b) - sqrt(delta)) / (2 * a))

print('Welcome to Quadratic Equation Solver Program!')
print('Write the following values:')
resp = eq2(int(input('a = ')), int(input('b = ')), int(input('c = ')))
print(resp)
