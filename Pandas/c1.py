import pandas as pd
# data ={
#     "name":["Arun","Aman","Anshuman","KM"],
#     "city":["Azamgarh","Maharajganj","Maharajganj","BKT"],
#     "course":["B.Tech","B.Tech","B.Tech","B.Tech"],
#     "marks":[88,89,87,90]
# }

# df = pd.DataFrame(data)
# print(df)

# print("head() fun")

# print(df.head())

# print("info() fun")

# print(df.info())

# print("describe() fun")

# print(df.describe())

# print("Save as csv file 'to_csv()'")
# df.to_csv("tech4bPandas")

studentDetail = pd.read_csv("Ak.csv")
df = pd.DataFrame(studentDetail)
# print(df)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())


# print(df.columns)

print(df[df["Marks"] > 50]["Marks"].to_list())
result = df.loc[df["Marks"] > 50 , ["Name","Marks"]]
print(result)