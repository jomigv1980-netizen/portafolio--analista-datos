import pandas as pd
import numpy as np
np.random.seed(42) # se utiliza solo para datos aleatoriospara que los datos que vamos a crear  salgan igual cada vez que se corran
fechas = pd.date_range("2025-01-01","2025-11-10", freq="D") # se crea un rango de fechas desde el 1 de enero de 2025 hasta el 10 de noviembre de 2025 con frecuencia diaria
categorias = ["Electronica","Ropa", "Hogar", "Deportes"] # se crean las categorias de los productos
regiones = ["Ciudad de Mexico", "Guadalajara", "Monterrey", "Puebla"] # se crean las regiones de venta
df = pd.DataFrame({
    "fecha": np.random.choice(fechas, size=1000), # se elige aleatoriamente 1000 fechas del rango de fechas creado
    "categoria":np.random .choice(categorias,size=1000), # se elige aleatoriamente 1000 categorias del rango de categorias creado
    "region":np.random.choice(regiones,size=1000), # se elige aleatoriamente 1000 regiones del rango de regiones creado
    "ventas":np.random.randint(200,5000,1000), 
    "costo":np.random.randint(100,3500,1000), 
    "unidades":np.random.randint    (1,10,1000)
})
#Esto mete 2 errores a propósito, como en la vida real, guarda el archivo y te muestra las primeras filas.

df.loc[10,"ventas"]= None #Es para simular un dato que falta, como pasa en la vida real.
df.loc[25,"categoria"]= "electronica" # pone la categoría en minúscula y sin acento. Es para simular un dato escrito mal, inconsistente.
df.to_csv("ventas.csv", index=False) #Guarda tu tabla como archivo ventas.csv en tu carpeta. El index=False es para que no guarde una columna extra con los números de fila.
print(df.head()) #Te muestra las primeras 5 filas para que veas cómo quedó la tabla.
print("Filas:", len(df)) #Te dice cuántas filas tiene tu tabla.

df["fecha"] = pd.to_datetime(df["fecha"])  # Convierte la columna fecha a formato fecha para poder agrupar por mes
df["categoria"] = df["categoria"].str.lower().str.capitalize()  # Pone todas las categorias en minuscula y luego la primera en mayuscula, para corregir electronica
df = df.dropna()  # Borra las filas que tienen algun dato vacio, como la fila 10
df["margen"] = df["ventas"] - df["costo"]  # Crea la columna margen, es ventas menos costo
df["mes"] = df["fecha"].dt.to_period("M")  # Crea la columna mes, solo año y mes, para ver ventas por mes

print(df.head())  # Te muestra las primeras 5 filas para que veas cómo quedó la tabla después de limpiar los datos.
print("Filas despues de limpiar datos:", len(df)    )  # Te dice cuántas filas tiene tu tabla después de limpiar los datos.
print(df["categoria"].unique()) # Te dice cuáles son las categorias que quedaron después de limpiar los datos. 

df.to_csv("ventas_limpias.csv", index=False)  # Guarda tu tabla limpia como archivo ventas_limpias.csv en tu carpeta. El index=False es para que no guarde una columna extra con los números de fila.   


print("total ventas:", df["ventas"].sum() )  # Te dice el total de ventas
print("total margen:", df["margen"].sum() )  # Te dice el total de margen
print(df.groupby("categoria")["ventas"].sum().sort_values(ascending=False) )  # Te dice el total de ventas por categoria
print(df.groupby("region")["ventas"].sum().sort_values(ascending=False) )  # Te dice el total de ventas por region
print(df.groupby("mes")["ventas"].sum().sort_values(ascending=False) )  # Te dice el total de ventas por mes