import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z1 = np.add(x, y)
z2 = np.subtract(x, y)
z3 = np.multiply(x, y)
z4 = np.divide(x, y)
z5 = np.power(x, y)
z6 = np.mod(x, y)
z7 = np.divmod(x, y)
z8 = np.absolute(x)

a = [-2.3232,3.33233,-4.8789,-2.34275]
z9 = np.trunc(a)
z10 = np.fix(a) #does the same work as trunch
z11 = np.around(a,2)
z12 = np.floor(a)
z13 = np.ceil(a)

print(z1)
print(z2)
print(z3)
print(z4)
print(z5)
print(z6)
print(z7)
print(z8)
print(z9)
print(z10)
print(z11)
print(z12)
print(z13)
