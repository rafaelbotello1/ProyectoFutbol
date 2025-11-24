import pandas as pd
import joblib
import numpy as np

model = joblib.load("modelo.pkl")
df = pd.read_excel("scripts/datos_nuevos_partidos.xlsx")
X = df[["pos_local", "pos_visitante", "gf_local", "gf_visitante"]]
preds = model.predict_proba(X)  # preds es una lista de 3 arrays con forma (10, 2)

# Verificación de estructura
print("Número de arrays en preds:", len(preds))  # Debe ser 3
print("Forma de preds[0]:", np.array(preds[0]).shape)  # Debe ser (10, 2)

resultados = []
for i, partido in df.iterrows():
    # Cada preds[j][i][1] corresponde a la probabilidad de la clase j
    prob_local = round(float(preds[0][i][1]), 2)    # Local gana
    prob_empate = round(float(preds[1][i][1]), 2)    # Empate
    prob_visitante = round(float(preds[2][i][1]), 2) # Visitante gana

    resultados.append({
        "local": partido["local"],
        "visitante": partido["visitante"],
        "fecha": partido["fecha"],
        "prob_local_gana": prob_local,
        "prob_empate": prob_empate,
        "prob_visitante_gana": prob_visitante
    })

df_pred = pd.DataFrame(resultados)
df_pred.to_csv("backend/predicciones.csv", index=False)
print("✅ Predicciones generadas en predicciones.csv")