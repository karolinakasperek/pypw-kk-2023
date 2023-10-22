import pandas as pd

# data = {
   #  'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    # 'Age': [25, 30, 30, 40, 45],
    # 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# }

# df = pd.DataFrame(data)
# df.to_excel("example.xlsx")
# print(df)

df = pd.read_csv("users.csv")
df["New age"] = df.apply(lambda x: x["Age"] + 1, axis=1)
print(df)
