import pandas as pd

df = pd.read_csv("denue_inegi_43_.csv", encoding="latin-1")

df =df[["codigo_act", "nombre_act", "entidad", "municipio", "latitud", "longitud", "fecha_alta"]]

print(df.head())
df.to_csv("cleaned.csv")