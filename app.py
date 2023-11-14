from flask import Flask, render_template
import os

app = Flask(__name__)

##@app.route('/')
##def index():
    #return "que maricada"
  ##  recursos =['PHP','PYTHON','JAVA', 'DART']
    ##data = {
       ## 'titulo':'gil',
       ## 'bienvenida':'!saludos!',
       ## 'recursos':recursos,
      ##  'numero_recursos': len(recursos)
    ##}
@app.route('/')
def pagina1():
    return render_template('pagina1.html')

@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')


   ## return render_template('index.html', data=data)
if __name__ == "__main__":
    app.run("0.0.0.0", 8081, debug=True)
