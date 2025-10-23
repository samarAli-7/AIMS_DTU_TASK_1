# ONE HOT ENCODING WITHOUT USING ANY HELPER/PRE-DEFINED FUNCTIONS

import pandas as pd


data = {
    "Color": ["Red", "Green", "Blue", "Green", "Red","Blue"]
}

df = pd.DataFrame(data)

categories = ["Red","Green","Blue"]

for category in categories:
    encoder = []
    for value in df["Color"]:
        if value == category:
            encoder.append(1)
        else:
            encoder.append(0)
    df[category] = encoder

print()
print(df)

'''
here:-
red = [1,0,0]
blue = [0,0,1]
green = [0,1,0]
'''



# dropping first column for dummy_variable_trap

df = df.drop("Red", axis=1)
print()
print(df)


'''
here:-
red = [0,0]
blue = [0,1]
green = [1,0]
'''