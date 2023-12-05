from flask import Flask, render_template, request, redirect, url_for

import os

app = Flask(__name__)
@app.route('/')
def index():
    #return "si funciono"
    #recursos =['PHP','PYTHON','JAVA', 'DART']
    #data = {
     #   'titulo':'kajsnd',
     #   'bienvenida':'!saludos!',
    #  'recursos':recursos,
     #   'numero_recursos': len(recursos)
    #}    
    #return render_template('index.html', data=data)



    return render_template('index.html')

@app.route('/reservas')
def reservas():
    return render_template('reservas.html')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        tipo_documento = request.form['tipo_documento']
        numero_documento = request.form['numero_documento']
        correo = request.form['correo']
        password = request.form['password']
        # Agrega lógica de almacenamiento de usuarios (puedes personalizar esto)
        return redirect(url_for('index'))
    return render_template('registro.html')


@app.route('/novedades')
def novedades():
    return render_template('novedades.html')


def verificar_credenciales(email, password):
    # Aquí verificarías las credenciales (por ejemplo, con una base de datos)
    return email == 'ing.davidsotelo19@gmail.com' and password == '123456'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if verificar_credenciales(email, password):
            # Si las credenciales son correctas, redirigir al dashboard
            return redirect(url_for('dashboard'))
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Aquí iría la lógica de tu página de dashboard
    return render_template('dashboard.html')

@app.route('/Habidisponible')
def Habidisponible():
    return render_template('Habidisponible.html')

if __name__ == "__main__":
    app.run("0.0.0.0", 8081, debug=True)
    
    
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Manejo de error general
@app.errorhandler(Exception)
def handle_exception(error):
    return render_template('error.html', error=error), 500
