from flask import Flask

app = Flask(__name__)

#routers

@app.route('/')
def index():
    return '<h1> My store</h1>'

#run de la aplicacion 

if __name__  == '__main__':
    app.run(debug=True)