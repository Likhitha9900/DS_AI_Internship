import numpy as np
marks=np.array([[60,70,30],[31,24,56],[68,90,58]])
print(marks)
print(np.median(marks))
print("shape:",marks.shape)
result=np.median(marks,axis=1)
print(result)
result=np.median(marks,axis=0)
print(result)

import numpy as np
marks=np.array([[2,3,4],[5,6,7],[9,0,1]])
print(marks)
print(np.median(marks))
row=np.median(marks,axis=1)
print(row)
col=np.median(marks,axis=0)
print(col)