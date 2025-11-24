
import pandas as pd
from random import randint, sample, choice
from datetime import datetime, timedelta

equipos = ["America", "Chivas", "Tigres", "Pumas", "Cruz Azul", "Leon", "Atlas", "Toluca", "Puebla", "Santos", "Tijuana", "Queretaro", "Mazatlan", "Necaxa", "Juarez", "San Luis"]
partidos = []
usados = set()
base_fecha = datetime(2024, 7, 1)

for i in range(100):
    while True:
        local, visitante = sample(equipos, 2)
        fecha = base_fecha + timedelta(days=i)
        if (local, visitante, fecha.date()) not in usados:
            usados.add((local, visitante, fecha.date()))
            pos_local = randint(1, 18)
            pos_visitante = randint(1, 18)
            gf_local = randint(10, 35)
            gf_visitante = randint(10, 35)
            resultado = choice(["local", "empate", "visitante"])
            local_gana = 1 if resultado == "local" else 0
            empate = 1 if resultado == "empate" else 0
            visitante_gana = 1 if resultado == "visitante" else 0
            partidos.append({
                "local": local, "visitante": visitante, "fecha": fecha.date(),
                "pos_local": pos_local, "pos_visitante": pos_visitante,
                "gf_local": gf_local, "gf_visitante": gf_visitante,
                "local_gana": local_gana, "empate": empate, "visitante_gana": visitante_gana
            })
            break

df = pd.DataFrame(partidos)
df.to_csv("datos_partidos.csv", index=False)
print("✅ Archivo 'partidos.csv' generado con 100 partidos.")
