
import pandas as pd

# Cargar archivos
csv_path = "datos_partidos.csv"
xlsx_path = "datos_nuevos_partidos.xlsx"

df_existente = pd.read_csv(csv_path)
df_nuevos = pd.read_excel(xlsx_path)

# Eliminar duplicados (mismo local, visitante y fecha)
df_final = pd.concat([df_existente, df_nuevos], ignore_index=True)
df_final.drop_duplicates(subset=["local", "visitante", "fecha"], inplace=True)

df_final.to_csv(csv_path, index=False)
print("✅ Nuevos partidos agregados correctamente a partidos.csv")
