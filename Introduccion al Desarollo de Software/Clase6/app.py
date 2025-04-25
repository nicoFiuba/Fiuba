"""
1) Crear un primer proyecto en Flask. 
Escribir en el navegador “Hola Mundo”
2)Continuar con este mismo proyecto, y en la vista donde escribieron hola mundo, incorporar debajo un link que lleve a una nueva vista llamada howiam.html que tenga un texto con una breve reseña del alumno.
"""

from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    howiam= url_for('howiam')

    return f'Hello, World! <a href = "{howiam}">Quien soy?</a>'

@app.route('/howiam')
def howiam():
    return render_template('howiam.html')

if __name__ == '__main__':
    app.run("localhost", port=8081, debug=True) # esto solo funca usando python3 app.py
