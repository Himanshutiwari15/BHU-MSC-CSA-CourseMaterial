import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


x = random.randint(100)
f = random.rand()
arr = random.randint(100,size=(5))
arrf = random.rand(5)
choose = random.choice(arr)
choose = random.choice(arr,size=(2))
probability_arr = random.choice([1,2,3,4],p=[0.1,0.3,0.6,0],size=(7))
#sns.distplot([0,1,2,3,4,5,6,7])
#plt.show()
#sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
#plt.show()
#x = random.normal(size=(2, 3))
#print(x)
#x = random.binomial(n=10, p=0.5, size=10)
#print(x)

print(x,f)
print(arr)
print(arrf)
print(choose)
print(probability_arr)
random.shuffle(arr)
print(arr)
print(random.permutation(arr))
print(arr)

