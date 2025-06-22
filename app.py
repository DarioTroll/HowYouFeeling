from flask import Flask, render_template, request, redirect, jsonify, session, url_for
from dotenv import load_dotenv
from functools import wraps
import os
import mysql.connector
import hashlib

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", os.urandom(24))

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Connessione al database
conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)
cursor = conn.cursor(dictionary=True)

# Try revert that hash...
users = {
    "dariotrollo": "61b0e03adc0eb4bba073fbc584e5ac23a195a49676fb21976acb055f8d4ecc45"
}

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# --- LOGIN ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = "dariotrollo"
        password = request.form['password']
        if username in users and users[username] == hash_password(password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template("login.html", error="Password errata")
    return render_template('login.html')

# --- LOGOUT ---
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# --- DECORATORE PER PROTEGGERE LE PAGINE ---
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- HOME ---
@app.route("/")
@login_required
def home():
    return render_template("home.html")


# --- INSERIMENTI ---
@app.route('/inserisci_dolore', methods=['GET', 'POST'])
@login_required
def inserisci_dolore():
    if request.method == 'POST':
        dati = {
            "data": request.form['data'],
            "ora": request.form['ora'],
            "viso": request.form.get('viso', 0),
            "testa_fronte": request.form.get('testa_fronte', 0),
            "testa_tempie_dx": request.form.get('testa_tempie_dx', 0),
            "testa_tempie_sx": request.form.get('testa_tempie_sx', 0),
            "testa_sommità": request.form.get('testa_sommità', 0),
            "testa_occipite": request.form.get('testa_occipite', 0),
            "nuca": request.form.get('nuca', 0),
            "mascella_dx": request.form.get('mascella_dx', 0),
            "mascella_sx": request.form.get('mascella_sx', 0),
            "denti": request.form.get('denti', 0),
            "collo": request.form.get('collo', 0),
            "spalla_dx": request.form.get('spalla_dx', 0),
            "spalla_sx": request.form.get('spalla_sx', 0),
            "braccio_superiore_dx": request.form.get('braccio_superiore_dx', 0),
            "braccio_superiore_sx": request.form.get('braccio_superiore_sx', 0),
            "braccio_inferiore_dx": request.form.get('braccio_inferiore_dx', 0),
            "braccio_inferiore_sx": request.form.get('braccio_inferiore_sx', 0),
            "gomito_dx": request.form.get('gomito_dx', 0),
            "gomito_sx": request.form.get('gomito_sx', 0),
            "polso_dx": request.form.get('polso_dx', 0),
            "polso_sx": request.form.get('polso_sx', 0),
            "mano_dx": request.form.get('mano_dx', 0),
            "mano_sx": request.form.get('mano_sx', 0),
            "dito_dx": request.form.get('dito_dx', 0),
            "dito_sx": request.form.get('dito_sx', 0),
            "petto_superiore_dx": request.form.get('petto_superiore_dx', 0),
            "petto_superiore_sx": request.form.get('petto_superiore_sx', 0),
            "petto_centrale": request.form.get('petto_centrale', 0),
            "pancia": request.form.get('pancia', 0),
            "addome_superiore": request.form.get('addome_superiore', 0),
            "addome_inferiore": request.form.get('addome_inferiore', 0),
            "schiena_superiore_dx": request.form.get('schiena_superiore_dx', 0),
            "schiena_superiore_sx": request.form.get('schiena_superiore_sx', 0),
            "schiena_inferiore_dx": request.form.get('schiena_inferiore_dx', 0),
            "schiena_inferiore_sx": request.form.get('schiena_inferiore_sx', 0),
            "sedere_dx": request.form.get('sedere_dx', 0),
            "sedere_sx": request.form.get('sedere_sx', 0),
            "gamba_superiore_dx": request.form.get('gamba_superiore_dx', 0),
            "gamba_superiore_sx": request.form.get('gamba_superiore_sx', 0),
            "ginocchio_dx": request.form.get('ginocchio_dx', 0),
            "ginocchio_sx": request.form.get('ginocchio_sx', 0),
            "polpaccio_dx": request.form.get('polpaccio_dx', 0),
            "polpaccio_sx": request.form.get('polpaccio_sx', 0),
            "caviglia_dx": request.form.get('caviglia_dx', 0),
            "caviglia_sx": request.form.get('caviglia_sx', 0),
            "piede_dx": request.form.get('piede_dx', 0),
            "piede_sx": request.form.get('piede_sx', 0)
        }

        query = f"""
            INSERT INTO Dolore (
                data, ora, viso, testa_fronte, testa_tempie_dx, testa_tempie_sx, testa_sommità,
                testa_occipite, nuca, mascella_dx, mascella_sx, denti, collo, spalla_dx, spalla_sx,
                braccio_superiore_dx, braccio_superiore_sx, braccio_inferiore_dx, braccio_inferiore_sx,
                gomito_dx, gomito_sx, polso_dx, polso_sx, mano_dx, mano_sx, dito_dx, dito_sx,
                petto_superiore_dx, petto_superiore_sx, petto_centrale, pancia, addome_superiore,
                addome_inferiore, schiena_superiore_dx, schiena_superiore_sx, schiena_inferiore_dx,
                schiena_inferiore_sx, sedere_dx, sedere_sx, gamba_superiore_dx, gamba_superiore_sx,
                ginocchio_dx, ginocchio_sx, polpaccio_dx, polpaccio_sx, caviglia_dx, caviglia_sx,
                piede_dx, piede_sx
            ) VALUES (
                %(data)s, %(ora)s, %(viso)s, %(testa_fronte)s, %(testa_tempie_dx)s, %(testa_tempie_sx)s, %(testa_sommità)s,
                %(testa_occipite)s, %(nuca)s, %(mascella_dx)s, %(mascella_sx)s, %(denti)s, %(collo)s, %(spalla_dx)s, %(spalla_sx)s,
                %(braccio_superiore_dx)s, %(braccio_superiore_sx)s, %(braccio_inferiore_dx)s, %(braccio_inferiore_sx)s,
                %(gomito_dx)s, %(gomito_sx)s, %(polso_dx)s, %(polso_sx)s, %(mano_dx)s, %(mano_sx)s, %(dito_dx)s, %(dito_sx)s,
                %(petto_superiore_dx)s, %(petto_superiore_sx)s, %(petto_centrale)s, %(pancia)s, %(addome_superiore)s,
                %(addome_inferiore)s, %(schiena_superiore_dx)s, %(schiena_superiore_sx)s, %(schiena_inferiore_dx)s,
                %(schiena_inferiore_sx)s, %(sedere_dx)s, %(sedere_sx)s, %(gamba_superiore_dx)s, %(gamba_superiore_sx)s,
                %(ginocchio_dx)s, %(ginocchio_sx)s, %(polpaccio_dx)s, %(polpaccio_sx)s, %(caviglia_dx)s, %(caviglia_sx)s,
                %(piede_dx)s, %(piede_sx)s
            )
        """

        try:
            with conn.cursor() as cursor:
                cursor.execute(query, dati)
            conn.commit()
            return jsonify({"success": True, "message": "Inserimento avvenuto con successo!"})
        except Exception as e:
            return jsonify({"success": False, "message": f"Errore: {str(e)}"})

    return render_template('inserisci_dolore.html')

@app.route("/inserisci_umore", methods=["GET", "POST"])
@login_required
def inserisci_umore():
    if request.method == "POST":
        data = request.form.get("data", 0)
        ora = request.form.get("ora", 0)
        ansia = request.form.get("ansia", 0)
        energia = request.form.get("energia", 0)
        soddisfazione = request.form.get("soddisfazione", 0)
        felicita = request.form.get("felicita", 0)
        stress = request.form.get("stress", 0)

        try:
            cursor.execute("""
                INSERT INTO Umore (data, ora, ansia, energia, soddisfazione, felicita, stress)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (data, ora, ansia, energia, soddisfazione, felicita, stress))
            conn.commit()
            return jsonify({"success": True, "message": "Inserimento umore avvenuto con successo!"})
        except Exception as e:
            return jsonify({"success": False, "message": f"Errore: {str(e)}"})

    return render_template("inserisci_umore.html")

@app.route("/inserisci_sonno", methods=["GET", "POST"])
@login_required
def inserisci_sonno():
    if request.method == "POST":
        data = request.form.get("data", 0)
        ora = request.form.get("ora", 0)
        ora_inizio = request.form.get("ora_inizio", 0)
        ora_fine = request.form.get("ora_fine", 0)
        qualita = request.form.get("qualita", 0)

        try:
            cursor.execute("""
                INSERT INTO Sonno (data, ora, ora_inizio, ora_fine, qualita)
                VALUES (%s, %s, %s, %s, %s)
            """, (data, ora, ora_inizio, ora_fine, qualita))
            conn.commit()
            return jsonify({"success": True, "message": "Inserimento sonno avvenuto con successo!"})
        except Exception as e:
            return jsonify({"success": False, "message": f"Errore: {str(e)}"})

    return render_template("inserisci_sonno.html")

# --- VISUALIZZAZIONE ---
@app.route("/visualizza_dolore")
@login_required
def visualizza_dolore():
    cursor.execute("SELECT * FROM Dolore")
    dati = cursor.fetchall()
    return render_template("visualizza_dolore.html", dati=dati)

@app.route("/visualizza_umore")
@login_required
def visualizza_umore():
    cursor.execute("SELECT * FROM Umore")
    dati = cursor.fetchall()
    return render_template("visualizza_umore.html", dati=dati)

@app.route("/visualizza_sonno")
@login_required
def visualizza_sonno():
    cursor.execute("SELECT * FROM Sonno")
    dati = cursor.fetchall()
    return render_template("visualizza_sonno.html", dati=dati)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
