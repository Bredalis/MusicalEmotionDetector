
# Detector de Emociones en Música (Clasificacion)

# Librerias

import pandas as pd



# Obtener datos

df = pd.read_excel("Songs.xlsx")
df =  df.head(30)

# Preparar los datos

df = df.drop(["ID", "Names"], axis = 1)

print("DF:", df)
print(df.columns)

for i in range(30):
	print(df["Lyrics "][i].lower())

print(df["Lyrics "])

# One Hot Encoding






# Dividir los datos






# Modelo






# Entrenamiento y prediccion



# Metricas







