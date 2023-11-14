from flask import Flask, render_template
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

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run("0.0.0.0", 8081, debug=True)
