from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'hola'

@app.route('/')
def index():
    usuario = "Nico"
    flash(f"Bienvenido {usuario}", "info") #metodos de flash: success, info, warning, error
    return render_template("index.html", active_page='index')

@app.route('/about')
def about():
    return render_template("about.html", active_page='about')

@app.route('/contact')
def contact():
    return render_template("contact.html", active_page='contact')

@app.route('/gallery')
def gallery():
    return render_template("gallery.html", active_page='gallery')

@app.route('/menu')
def menu():
    return render_template("menu.html", active_page='menu')

@app.route('/reservation')
def reservation():
    return render_template("reservation.html", active_page='reservation')

@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'POST':
        flash("Reserva realizada con éxito", "success")
        return redirect(url_for('reserva'))
        
    return render_template("reservation.html", active_page='reservation')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
   app.run(host="localhost", port=8080, debug=True)

