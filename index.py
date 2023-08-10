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

port= 10000

if __name__ == '__main__':
    app.run(debug=True)

