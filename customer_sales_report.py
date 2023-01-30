import pandas as pd

df = pd.read_csv("sales.csv")
salesreport = open("salesreport.csv", "a")


df["TotalPay"] = df["SubTotal"] + df["TaxAmt"] + df["Freight"]
Pay = df.groupby(["CustomerID"], as_index=False)[["TotalPay"]].sum()

lines = str(Pay)
salesreport.writelines(lines)

salesreport.close()

f = open("salesreport.csv", "r")
print(f.read())
