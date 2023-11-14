from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    #return "si funciono"
    #recursos =['PHP','PYTHON','JAVA', 'DART']
    #data = {
     #   'titulo':'gil',
     #   'bienvenida':'!saludos!',
    #  'recursos':recursos,
     #   'numero_recursos': len(recursos)
    #}    
    #return render_template('index.html', data=data)



    return render_template('index.html')

@app.route('/reservas')
def reservas():
    return render_template('reservas.html')

@app.route('/novedades')
def novedades():
    return render_template('novedades.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Aquí puedes agregar la lógica de autenticación con el correo y la contraseña
        # Por ahora, redirigimos a la página de inicio después del "login"
        return redirect(url_for('index'))
    return render_template('login.html')

if __name__ == "__main__":
    app.run("0.0.0.0", 8081, debug=True)
