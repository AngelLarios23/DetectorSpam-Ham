from flask import Flask, render_template, request
from model_spam import reconocer_spam
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db

# Inicializa la app de Firebase
credenciales = credentials.Certificate("firebase_key.json") # archivo de verificacion para acceder a Firebase
firebase_admin.initialize_app(credenciales, {
    'databaseURL': 'https://dbspam-ae2bc-default-rtdb.firebaseio.com/' # url de Firebase
})


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        texto = request.form["mensaje"]
        etiqueta = reconocer_spam(texto)
        resultado = f"Este mensaje es: {etiqueta.upper()}" # mensaje para avisar si es spam o ham

        mensaje_data = {
            "texto": texto,
            "etiqueta": etiqueta,
            "fecha": datetime.now().isoformat()
        }

        # Guarda en Firebase
        ref = db.reference("mensajes")
        ref.push(mensaje_data)

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
