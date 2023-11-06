from flask import Flask, render_template

app = Flask(__name__)

#routers

@app.route('/')
def index():
    return render_template('base.html')

#run de la aplicacion 

if __name__  == '__main__':
    app.run(debug=True)