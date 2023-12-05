from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
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
    conexion = mysql.connector.connect(**db_config)
    cursor = conexion.cursor()
    
    consulta = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
    cursor.execute(consulta, (email, password))
    usuario = cursor.fetchone()
    
    cursor.close()
    conexion.close()

    # Si se encuentra un usuario con las credenciales proporcionadas, retorna True
    return usuario is not None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if verificar_credenciales(email, password):
            # Si las credenciales son correctas, redirigir al dashboard
            return redirect(url_for('dashboard'))
        # Si las credenciales son incorrectas, redirigir al inicio de sesión nuevamente
        return redirect(url_for('index'))
    
    # Renderizar el formulario de inicio de sesión si es un GET
    return render_template('login.html')

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'laravel',
}

# Crear una conexión a la base de datos
conexion = mysql.connector.connect(**db_config)

# Verificar si la conexión fue exitosa
if conexion.is_connected():
    print('Conexión exitosa a la base de datos')

# Ejemplo de ruta para consultar datos desde la base de datos
@app.route('/consultar_datos')
def consultar_datos():
    cursor = conexion.cursor(dictionary=True)  # Usar cursores tipo diccionario para obtener resultados con nombres de columnas
    consulta = "SELECT * FROM nombre_de_tu_tabla"
    cursor.execute(consulta)
    datos = cursor.fetchall()
    cursor.close()
    return str(datos)  # Retorna los datos como una cadena (esto dependerá de cómo deseas mostrar los datos)






@app.route('/dashboard')
def dashboard():
    # Aquí iría la lógica de tu página de dashboard
    return render_template('dashboard.html')



if __name__ == "__main__":
    app.run("0.0.0.0", 8081, debug=True)
