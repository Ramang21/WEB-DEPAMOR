from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)
# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'depamor'

mysql = MySQL(app)

@app.route("/")
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        user = cursor.fetchone()
        # If account exists in accounts table in out database
        if user:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = user['id']
            session['username'] = user['username']
            # Redirect to home page
            return redirect(url_for('Dashboard'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)

@app.route("/Dashboard")
def Dashboard():
    return render_template('Dashboard.html')

@app.route("/Data")
def Data():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM registrasi_plat_motor ORDER BY id desc")
    dataplat = cursor.fetchall()
    return render_template('Data.html', dataplat=dataplat)

@app.route("/Registrasiplat", methods=['GET', 'POST'])
def maiRegistrasiplatn():
    if request.method=='POST':
        username = request.form['Username']
        nama = request.form['Nama']
        nomorplat = request.form['NomorPlat']
        status = request.form['Status']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("INSERT INTO registrasi_plat_motor (Username, Nama, NomorPlat, Status) VALUES (%s, %s, %s, %s)", (username, nama, nomorplat, status))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('Data'))
    return render_template('Registrasiplat.html')

@app.route("/Laporan")
def Laporan():
    return render_template('Laporan.html')

@app.route("/laporanmasuk")
def laporanmasuk():
    return render_template('laporanmasuk.html')

@app.route("/laporankeluar")
def laporankeluar():
    return render_template('laporankeluar.html')

@app.route("/Scanplat")
def Scanplat():
    return render_template('Scanplat.html')

@app.route("/scanmasuk")
def scanmasuk():
    return render_template('scanmasuk.html')

@app.route("/scankeluar")
def scankeluar():
    return render_template('scankeluar.html')

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)