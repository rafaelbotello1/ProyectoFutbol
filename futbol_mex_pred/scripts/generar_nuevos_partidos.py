
import pandas as pd
from random import randint, sample
from datetime import datetime, timedelta

equipos = ["America", "Chivas", "Tigres", "Pumas", "Cruz Azul", "Leon", "Atlas", "Toluca", "Puebla", "Santos", "Tijuana", "Queretaro", "Mazatlan", "Necaxa", "Juarez", "San Luis"]
partidos = []
fechas = [datetime(2025, 6, 8) + timedelta(days=i) for i in range(10)]
usados = set()

for fecha in fechas:
    while True:
        local, visitante = sample(equipos, 2)
        if (local, visitante, fecha.date()) not in usados:
            usados.add((local, visitante, fecha.date()))
            partidos.append({
                "local": local, "visitante": visitante, "fecha": fecha.date(),
                "pos_local": randint(1, 18), "pos_visitante": randint(1, 18),
                "gf_local": randint(10, 35), "gf_visitante": randint(10, 35)
            })
            break

df = pd.DataFrame(partidos)
df.to_excel("datos_nuevos_partidos.xlsx", index=False)
print("✅ Archivo 'nuevos_partidos.xlsx' generado.")
