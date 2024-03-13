# import pandas as pd
# path = "C:/Users/lokes/Downloads/archive/watson_shap_values_for_testset.csv"
# df = pd.read_csv(path)
# print(df)
# # df.to_csv(path)
# # limits = df.tail(5)
# # print(df.dtypes)
# # print(df.tail(5))
# # print("saved succesfully")
# # print(df.describe(include="all"))
# # print(df.info())
# print(df.columns)

import pandas as pd
import numpy as np
path = "c:/Users/lokes/Downloads/data.xlsx"
df = pd.read_excel(path)
# headers = ["S.NO","EVEN","ODD","MULTIPLY 5","MULTIPLY 3","MULTIPLY 4"]
# df.columns = headers
# df.drop([10],axis=0)
# df.drop([10], axis=0, inplace=True)
# df.dropna(inplace=True )
# print(df.head(5))
##replaces nan with number
# df["EVEN"].replace(np.nan,22,inplace=True)
##divides by 2
# df["MULTIPLY 4"] = df["MULTIPLY 4"]  /2
##rename
# df.rename(columns ={"MULTIPLY 4": "MULTIPLY 2"}, inplace=True)
##data normalization
# df["length"]=df["length"]/df["length"].max()
##number to categrocial
# bins = np.linspace(min(df["length"]),max(df["length"]),4)
# group_names = ["low","medium","high"]
# df["length-binned"] =pd.cut(df["length"],bins,labels=group_names,include_lowest=True)
##categorical to numbers
# pd.get_dummies(df["length"])
# df.describe()
##value counts
# index = pd.Index(df["length"])
# print(index.value_counts())
##boxplot
# import seaborn as sns
# box = sns.boxplot(x="length", y="E",data=df)
# print(box)
##scatterplot
# import matplotlib.pyplot as plt
# x = df["length"]
# y=df["E"]
# print(plt.scatter(x,y))
# print(plt.title("scatterplot along the x and y axis"))
# print(plt.xlabel("length"))
# print(plt.ylabel("width"))
##Group by
# grp = df.groupby("A").sum()
# print(grp)
##change all headings
# grp = df.groupby(["A","B"],as_index=False)
# by = grp.aggregate(np.sum)
# print(by)
## divides indivual names and data
# l=[['apple',1],['apple',2],['apple',2],['ball',1],['ball',1]]
# df_10 = pd.DataFrame(data=[[1, 1]], columns=["A", "B"])
# df_10.groupby("A")["B"].nunique()
# print(df_10)

# print(df)
