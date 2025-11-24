from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

predicciones = []

def generar_predicciones():
    # Aquí puedes conectar tu modelo Random Forest real
    equipos = [
        ('América', 'Pumas'),
        ('Chivas', 'Cruz Azul'),
        ('Tigres', 'Toluca'),
        ('Monterrey', 'Santos'),
        ('León', 'Atlas'),
        ('Queretaro', 'Mazatlan'),
        ('Tijuana','San Luis') 
    ]

    nuevas_predicciones = []
    for local, visitante in equipos:
        prob_local = round(random.uniform(0.3, 0.5), 2)
        prob_empate = round(random.uniform(0.2, 0.4), 2)
        prob_visitante = round(1 - prob_local - prob_empate, 2)
        nuevas_predicciones.append({
            'fecha': '2025-05-21',
            'local': local,
            'visitante': visitante,
            'prob_local_gana': prob_local,
            'prob_empate': prob_empate,
            'prob_visitante_gana': prob_visitante
        })
    return nuevas_predicciones

@app.route('/')
def index():
    return render_template('index.html', predicciones=predicciones)

@app.route('/actualizar', methods=['POST'])
def actualizar():
    global predicciones
    predicciones = generar_predicciones()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
