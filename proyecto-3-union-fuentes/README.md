# Proyecto 3 - Unión de 4 Fuentes

## Pregunta de negocio
¿Qué proveedor vende más y el descuento ayuda a vender más?

## Fuentes que unimos
1. Base de datos PostgreSQL `ventas_db` - Tabla `ventas` (5 ventas)
2. Base de datos PostgreSQL `productos_db` - Tabla `productos` (4 productos)
3. Excel `Descuentos.xlsx` - Descuento por producto
4. CSV `Clientes.csv` - Tipo de cliente y ciudad

## Qué hicimos
1. Conectamos Python con las 2 bases de PostgreSQL con `sqlalchemy` y `psycopg2`
2. Leímos el Excel con `pd.read_excel` y el CSV con `pd.read_csv`
3. Unimos las 4 fuentes con `pd.merge` por `id_producto` y por `id_cliente`
4. Calculamos la venta neta: `venta_neta = ventas * (1 - descuento)`
5. Sumamos la venta neta por proveedor y por descuento

## Resultados

### ¿Qué proveedor vende más?
* Proveedor A: 5460.0 - Es el que más vende
* Proveedor B: 1360.0
* Proveedor C: 1140.0

### ¿El descuento ayuda a vender más?
No. El descuento más alto no es el que más vende.

* Descuento 10%: 4950.0 - Es el que más vende
* Descuento 20%: 1360.0 - Es el descuento más grande, pero no es el que más vende
* Descuento 5%: 1140.0
* Descuento 15%: 510.0 - Es el que menos vende

Conclusión: Lo que vende es el producto, en este caso la Laptop del Proveedor A, no el descuento. Dar 20% de descuento no hizo que se vendiera más.

## Archivos
* `analisis.py` - Código con todo el proceso
* `tabla_final_unida.csv` - Tabla final con las 4 fuentes unidas y la columna `venta_neta`
* `Descuentos.xlsx` - Archivo Excel de descuentos
* `Clientes.csv` - Archivo CSV de clientes

## Herramientas
Python, pandas, PostgreSQL, Docker, Excel, CSV, GitHub