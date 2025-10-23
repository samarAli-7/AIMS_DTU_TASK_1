# ORDINAL ENCODING WITHOUT USING ANY HELPER/PRE-DEFINED FUNCTIONS

import pandas as pd

data = {
    "Grade": ["Excellent", "Average", "Good", "Average", "Excellent", "Good"]
}

df = pd.DataFrame(data)
print()
print("Original DataFrame:")
print(df)



# print(categories)

encoded = []
# print(encoded)


for i in data["Grade"]:
    if i == "Excellent":
        encoded.append(2)
    elif i == "Good":
        encoded.append(1)
    elif i == "Average":
        encoded.append(0)

# print(encoded)


df["Encoded"] = encoded
print()
print("Encoded DataFrame:")
print(df)   






'''
OR 

'''




# this will not map as excellent > good > average mathematically but is better because no if-else , basically scalable

categories = list(set(df["Grade"]))
 
mapping = {}
for index, category in enumerate(categories):
    mapping[category] = index


encoded = []
for value in df["Grade"]:
    encoded.append(mapping[value])

df["Encoded"] = encoded
print()
print(df)