import pandas as pd

data = {
    "Area": ["Oslo", "Bærum", "Lørenskog"],
    "Price_NOK": [5000000, 7000000, 4500000]
}

df = pd.DataFrame(data)

print(df)
