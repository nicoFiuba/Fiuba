from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    nombre = "Nicolas"
    apellido = "Feldman"
    print(nombre, apellido)
    return render_template("home.html", nombre = nombre, apellido = apellido)

@app.route('/recetas')
def Recetas():
    return render_template("recetas.html")

@app.route('/mireceta{id}')
def Mireceta():
    return render_template("mireceta{id}.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/reservation')
def reservation():
    return render_template("reservation.html")


if __name__ == '__main__':
   app.run(host="localhost", port=8080, debug=True)

