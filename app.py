#importación del framework
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

#inicialización del framework (app)
app= Flask(__name__)
#ingreso de las credenciales para el acceso a la bd
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='proyecto_medicos' 
app.secret_key='mysecretkey'
mysql= MySQL(app)

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

@app.route('/addmedicos')
def addmedicos():
    return render_template('addmedicos.html')

@app.route('/addmedicosguardar', methods=['POST'])
def addmedicosguardar():
    if request.method == 'POST':
        # pasamos a variables el contenido de los input
        Vnombre= request.form['txtnombre']
        Vap= request.form['txtap']
        Vam= request.form['txtam']
        Vrfc=request.form['txtrfc']
        Vcedula=request.form['txtcedula']
        Vemail=request.form['txtemail']
        # Conectar y ejecutar el insert
        CS = mysql.connection.cursor() # objeto de tipo cursor
        CS.execute('insert into medicos (nombre, ap, am, rfc, cedula, email) values (%s, %s, %s, %s, %s, %s)',(Vnombre, Vap, Vam, Vrfc, Vcedula, Vemail))
        mysql.connection.commit()
    return redirect(url_for('addmedicos'))

#ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)