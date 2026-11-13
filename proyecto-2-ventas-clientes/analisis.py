import pandas as pd #libreria para trabajar con datos en forma de tablas
import numpy as np #libreria para trabajar con datos numericos

url_clientes = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"  # Direccion de internet donde esta la informacion real de clientes
clientes = pd.read_csv(url_clientes, sep="|")  # Se lee la informacion de clientes desde internet y se guarda en la variable clientes, el separador es "|"
print(clientes.head())  # Muestra las primeras 5 filas de la tabla clientes
print("Clientes:", len(clientes)) # Muestra cuantas filas tiene la tabla clientes

np.random.seed(42) # se utiliza solo para datos aleatoriospara que los datos que vamos a crear  salgan igual cada vez que se corran
ventas= pd.DataFrame({ #empieza a crear la tabla de ventas con datos aleatorios
    "user_id":np.random.choice(clientes["user_id"], size=2000), # se elige aleatoriamente 2000 user_id de la tabla clientes
    "categoria":np.random.choice(["Electronica","Ropa", "Hogar", "Deportes"],size=2000), # se elige aleatoriamente 2000 categorias de productos
    "ventas":np.random.randint(200,5000,2000)  # se elige aleatoriamente 2000 valores de ventas
})

#AQUI SE CRUZAN LAS TABLAS DE VENTAS Y CLIENTES
df_cruzado = pd.merge(ventas,clientes, on="user_id", how="left") # se cruzan las tablas ventas y clientes por la columna user_id, se hace un left join para que queden todas las filas de ventas y solo las que coinciden de clientes
print(df_cruzado.head()) # Muestra las primeras 5 filas de la tabla cruzada
print("Filas Cruzadas:",len(df_cruzado)) # Muestra cuantas filas tiene la tabla cruzada

print(df_cruzado.groupby("occupation")["ventas"].sum().sort_values(ascending=False)) # Muestra el total de ventas por ocupacion, ordenado de mayor a menor
print(df_cruzado.groupby("gender")["ventas"].sum().sort_values(ascending=False)) # Muestra el total de ventas por genero, ordenado de mayor a menor
print(df_cruzado.groupby("categoria")["ventas"].sum().sort_values(ascending=True)) # Muestra el total de ventas por categoria, ordenado de menor a mayor

df_cruzado.to_csv("ventas_clientes_cruzado.csv", index=False) # Guarda la tabla cruzada como archivo ventas_clientes_cruzado.csv en tu carpeta. El index=False es para que no guarde una columna extra con los números de fila.
print("Archivo ventas_clientes_cruzado.csv guardado") # Muestra un mensaje indicando que el archivo se guardo
