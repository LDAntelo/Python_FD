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

@app.route('/grecco')
def grecco():
    return render_template('grecco.html')

@app.route('/vergara')
def vergara():
    return render_template('vergara.html')

@app.route('/nicobatlle')
def nicobatlle():
    return render_template('nicobatlle.html')

@app.route('/corrales')
def corrales():
    return render_template('corrales.html')

@app.route('/caraguata')
def caraguata():
    return render_template('caraguata.html')

@app.route('/pruebascorrales')
def pruebascorrales():
    return render_template('pruebascorrales.html')

if __name__ == '__main__':
    #app.run(debug=True)
    from waitress import serve
    serve(app,host="0.0.0.0",port=10000, threads=100)