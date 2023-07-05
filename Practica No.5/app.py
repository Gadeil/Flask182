# IMPORTAR LA LIBRERIA QUE SE NECESITA
from flask import Flask, render_template, request, redirect, url_for,flash
from flask_mysqldb import MySQL     


# Inicializacion del servidor Flask
app= Flask (__name__)
# sevidor para conectarse a la bdflask 
app.config['MySQL_HOST'] = "localhost"
app.config['MySQL_USER'] = "root"
app.config['MySQL_PASSWOR'] = ""
app.config['MySQL_BD'] = "bdflask"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

# Declaracion de rutas 

# Ruta Index http: http://localhost:5000
# La ruta se compone de nombre y la funcion 
@app.route('/')

def index():
    curSelect= mysql.connection.cursor()
    curSelect.execute('select * from albums')
    consulta= curSelect.fetchall()
    print

# La ruta ocupa de una funcion para funcionar 
def index():
    return render_template('index.html')

# Guardar
@app.route('/guardar', methods=['POST'])

def aguardar():
    
    if request.method == 'POST':
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
        #print(titulo,artista,anio)
        
        # es una variable de tipo cursor que contiene las variables 
        cs = mysql.connection.cursor()
        cs.execute('insert into album(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
        mysql.connection.commit()
        
    flash('Album agregado :)')
    return redirect(url_for('index'))

# Eliminar
@app.route('/eliminar')
def eliminar():
    return "se elimino el album de la bd"

# Ejecusion 
if __name__=='__main__':
    app.run(port=5000, debug=True)
    
@app.route('/editar/<id>')
def editar(id):
    cureditar= mysql.connection.cursor()
    cureditar.execute('select * from albums where id = %s', (id,))
    consulID= cureditar.fetchone()
    
    #redirecionamos para editar Album de html
    return render_template('EditarAlbum.html', album= consulID)
    

@app.route('/actualizar/<id>', methods=['POST'])

def actualizar(id):
    
    if request.method == 'POST':
        
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
        
        curAct= mysql.connection.cursor()
        curAct.execute('update albums set titulo=%s, artista=%s, anio=%s where id=%s', (Vtitulo, Vartista, Vanio, id,))
        mysql.connection.commit()
        
        flash('Album Actualizado en BD :)')
    return redirect(url_for('index'))    