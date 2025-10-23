# MEAN VALUE IMPUTATION WITHOUT USING ANY HELPER/PRE-DEFINED FUNCTIONS

import pandas as pd
import numpy as np


data = {
    "Physics": [np.nan, 92, 80, np.nan, 85],
    "Chemistry": [70, 90, np.nan, 88, np.nan],
    "Maths": [85, np.nan, 78, 90, np.nan]
}
print("ORIGINAL :-")
df = pd.DataFrame(data)
print(df)
for column in df.columns:
    total = 0
    n = 0
    for val in df[column]:
        if not np.isnan(val):
            total += val
            n += 1
    mean_val = total / n
    
    
    new_column = []
    for val in df[column]:
        if np.isnan(val):
            new_column.append(mean_val)
        else:
            new_column.append(val)
    # print(new_column)
    df[column] = new_column
print()
print("IMPUTED :-")
print(df)
