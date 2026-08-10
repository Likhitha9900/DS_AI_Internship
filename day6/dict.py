import pandas as pd
import numpy as np
x=[1,2,3,4,5]
y=pd.Series(x)
print(y)

x=np.array([10,20,30,40,50])
y=pd.Series(x)
print(y)

x={'a':10,'b':20,'c':30,'d':40,'e':50}
y=pd.Series(x)
print(y)

z={'name':'Alice', 'age':25, 'city':'New York'}
y=pd.Series(z)
print(y)

marks=[28,45,78]
x=pd.Series(marks,index=["maths","science","english"])
print(x)
print(x.tolist())