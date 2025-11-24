
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("scripts/datos_partidos.csv")
X = df[["pos_local", "pos_visitante", "gf_local", "gf_visitante"]]
y = df[["local_gana", "empate", "visitante_gana"]]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
joblib.dump(model, "modelo.pkl")
print("✅ Modelo entrenado y guardado como modelo.pkl")
