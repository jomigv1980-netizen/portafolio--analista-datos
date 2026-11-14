
import pandas as pd
import numpy as np
from sqlalchemy import create_engine #Importa create_engine, para conectar Python con PostgreSQL

motor_ventas = create_engine("postgresql+psycopg2://postgres:admin123@localhost:5433/ventas_db")  # Conecta Python con la base ventas_db usando psycopg2
motor_productos = create_engine("postgresql+psycopg2://postgres:admin123@localhost:5433/productos_db")  # Conecta Python con la base productos_db usando psycopg2
ventas = pd.read_sql("SELECT * FROM ventas", motor_ventas) #Lee la tabla ventas de la base ventas_db y la guarda en la variable ventas
productos = pd.read_sql("SELECT * FROM productos", motor_productos) #Lee la tabla productos de la base productos_db y la guarda en la variable productos
print(productos.head()) #Muestra las primeras 5 filas de la tabla productos
print(ventas.head()) #Muestra las primeras 5 filas de la tabla ventas

#vamos a leer los archivos de excel y .csv

descuentos = pd.read_excel("Descuentos.xlsx") #Lee el archivo descuentos.xlsx y lo guarda en la variable descuentos
clientes = pd.read_csv("Clientes.csv") #Lee el archivo clientes.csv y lo guarda en la variable clientes
print(descuentos.head()) #Muestra las primeras 5 filas de la tabla descuentos
print(clientes.head()) #Muestra las primeras 5 filas de la tabla clientes


#Une ventas con productos por id_producto para saber el nombre y proveedor de cada venta

ventas_productos = pd.merge(ventas, productos, on="id_producto") #Une la tabla ventas con la tabla productos por la columna id_producto y lo guarda en la variable ventas_productos
print(ventas_productos.head()) #Muestra las primeras 5 filas de la tabla ventas_productos


#nos falta pegar el Excel de descuentos, para saber qué descuento tenía cada producto.
ventas_completo =pd.merge(ventas_productos, descuentos, on="id_producto") # Une ventas_productos con descuentos por id_producto para saber el descuento de cada venta
print(ventas_completo.head()) #Muestra las primeras 5 filas de la tabla ventas_completo


#UNIUN DE CLIENTES .XLSX
tabla_final = pd.merge(ventas_completo, clientes, on="id_cliente") # Une ventas_completo con clientes por id_clientes para saber el nombre y correo de cada cliente
print(tabla_final.head())

#CALCULAMOS LA VENTA NETA 
tabla_final["venta_neta"] = tabla_final["ventas"] * (1 - tabla_final["descuento"])  # Crea una nueva columna venta_neta dentro de tabla_final con lo que realmente ganó la empresa
print(tabla_final.head())  # Muestra la tabla final ya con la columna venta_neta

# Suma la venta neta de cada proveedor para saber cuál vende más de verdad
venta_neta_proveedor = tabla_final.groupby("proveedor")["venta_neta"]. sum().sort_values(ascending=False)  # Agrupa la tabla final por proveedor y suma la venta_neta de cada uno, luego lo ordena de mayor a menor
print(venta_neta_proveedor)  # Muestra la venta neta de cada proveedor

# agrupando por descuento en lugar de por proveedor. Así vemos si a más descuento, más venta neta.
venta_neta_descuento = tabla_final.groupby("descuento")["venta_neta"]. sum().sort_values(ascending=False)  # Agrupa la tabla final por descuento y suma la venta_neta de cada uno, luego lo ordena de mayor a menor
print(venta_neta_descuento)  # Muestra la venta neta de cada descuento

#GUARDAMOS LA TABLA FINAL EN UN ARCHIVO CSV Y EN GITHUB
tabla_final.to_csv("tabla_final_unida.csv", index=False)  # Guarda la tabla final como archivo tabla_final.csv en tu carpeta. El index=False es para que no guarde una columna extra con los números de fila.
print("Archivo tabla_final.csv guardado")  # Muestra un mensaje indicando que el archivo