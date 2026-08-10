import pandas as pd
x = {"math": 80, "sci": 85, "eng": 90}
y = pd.Series(x, index=["eng"])
print(y)