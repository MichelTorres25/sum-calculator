import pandas as pd

# Leer archivo Excel
df = pd.read_excel("datos_con_problemas.xlsx")

 

# Mostrar datos originales
print("Datos originales:")
print(df)

# 1. Limpiar las fechas (convertir a datetime)
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')

# 2. Limpiar la columna 'Cantidad' (convertir a numérico, forzar valores inválidos a NaN)
df['Cantidad'] = pd.to_numeric(df['Cantidad'], errors='coerce')

# 3. Limpiar la columna 'PrecioUnitario' (convertir a numérico, forzar valores inválidos a NaN)
df['PrecioUnitario'] = pd.to_numeric(df['PrecioUnitario'], errors='coerce')

# 4. Rellenar valores nulos en la columna 'Nombre' con un valor predeterminado
df['Nombre'] = df['Nombre'].fillna('Desconocido')

# 5. Reemplazar valores nulos en 'Comentario' por 'Sin comentarios'
df['Comentario'] = df['Comentario'].fillna('Sin comentarios')

# 6. Verificar si hay valores negativos en la columna 'Cantidad' y corregir si es necesario
df['Cantidad'] = df['Cantidad'].apply(lambda x: abs(x) if isinstance(x, (int, float)) and x < 0 else x)

# Mostrar los datos limpios
print("\nDatos limpiados:")
print(df)
