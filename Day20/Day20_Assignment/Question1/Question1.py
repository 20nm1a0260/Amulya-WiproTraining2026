
import numpy as np
import pandas as pd

students = [
{"name": "Alice", "score": 85},
{"name": "Bob", "score": 92},
{"name": "Charlie", "score": 78},
{"name": "David", "score": 90},
{"name": "Eva", "score": 88}
]

df=pd.DataFrame(students)
arr=np.array(df)
scores=df["score"].to_numpy()
print(scores)
print("mean:",np.mean(scores))
print("median:",np.median(scores))
print("standard deviation:",np.std(scores))
df["above_average"]=df["score"]>np.mean(scores)
print(df)
