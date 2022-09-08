import pandas
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pandas.read_csv("cleaned.csv", encoding="latin-1")
df_filtrado = df["entidad"].value_counts()
df_filtrado = df_filtrado.to_frame()
df_filtrado.reset_index(inplace=True)
#print(df_filtrado.describe())
sns.set()
fig = px.bar(df_filtrado, x="entidad", y="index", orientation="h", height=1000)

#sns.barplot(x=[3,2,1], y=["A", "B", "C"])