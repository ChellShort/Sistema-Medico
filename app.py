#importación del framework
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

#inicialización del framework (app)
app= Flask(__name__)

#declaración de la ruta principal (index) http://localhost:5000
@app.route('/')
def index(): #metodo index
    return render_template('LOGIN.html') #el metodo index nos lleva a LOGIN.html

#ruta http://localhost:5000/guardar tipo POST para Insert
@app.route('/diagnosticos')
def diagnosticos():
    return render_template('diagnosticos.html')

@app.route('/exploraciones')
def exploraciones():
    return render_template('exploraciones.html')

@app.route('/pacientes')
def pacientes():
    return render_template('pacientes.html')

#ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)