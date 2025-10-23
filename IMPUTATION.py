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
print("IMPUTED(MEAN) :-")
print(df)







data = {
    "Physics": [np.nan, 92, 80, np.nan, 85],
    "Chemistry": [70, 90, np.nan, 88, np.nan],
    "Maths": [85, np.nan, 78, 90, np.nan]
}
df = pd.DataFrame(data)


for column in df.columns:
    sorted_values = []
    for value in df[column]:
        if not np.isnan(value):
            sorted_values.append(value)
            # print(sorted_values)
        # else:
        #     print("didnt found a number")
    sorted_values.sort()

    # print(sorted_values)
    n = len(sorted_values)

    if n % 2 == 1:
        median = sorted_values[n // 2]
    else:  
        median = (sorted_values[n//2 - 1] + sorted_values[n//2]) / 2
    new_column = []
    for value in df[column]:
        if np.isnan(value):
            new_column.append(median)
        else:
            new_column.append(value)
    # print(new_column)
    df[column] = new_column

print()
print("IMPUTED(MEDIAN) :-")
print(df)



