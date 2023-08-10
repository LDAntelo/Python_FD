from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Contacto')
def about():
    return render_template('about.html')

@app.route('/casupa')
def casupa():
    return render_template('casupa.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

if __name__ == '__main__':
    from waitress import serve
    serve(app,host="0.0.0.0",port=10000)