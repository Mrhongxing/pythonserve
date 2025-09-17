import pandas as pd
df = pd.read_excel("附件.xlsx","Sheet1",engine="openpyxl")
print(df.head(100))
with open("a.txt","a")as a:
    a.write(str(df.head(100)))