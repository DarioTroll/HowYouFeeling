import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, time

# Carica variabili ambiente
load_dotenv()

def calcola_ore_sonno(datetime_inizio_str, datetime_fine_str):
    try:
        fmt = "%Y-%m-%d %H:%M:%S"
        dt_inizio = datetime.strptime(datetime_inizio_str, fmt)
        dt_fine = datetime.strptime(datetime_fine_str, fmt)

        # Se l'orario di fine è prima dell'inizio, considera il giorno dopo (opzionale)
        if dt_fine < dt_inizio:
            dt_fine += timedelta(days=1)

        durata = dt_fine - dt_inizio
        ore = round(durata.total_seconds() / 3600, 2)  # ore con 2 decimali
        return ore

    except Exception as e:
        print(f"[Errore] Calcolo ore fallito per valori: ora_inizio={datetime_inizio_str}, ora_fine={datetime_fine_str} -> {e}")
        return 0

# Le funzioni seguenti servono solo per l'esecuzione standalone
def aggiorna_singola_riga(codice, ora_inizio, ora_fine, cursor):
    ore_di_sonno = calcola_ore_sonno(ora_inizio, ora_fine)
    cursor.execute("""
        UPDATE Sonno SET OreDiSonno = %s WHERE codice = %s
    """, (ore_di_sonno, codice))


def aggiorna_tutte_le_righe():
    import mysql.connector

    # Connessione al database tramite dotenv
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT codice, ora_inizio, ora_fine FROM Sonno")
    righe = cursor.fetchall()

    for riga in righe:
        aggiorna_singola_riga(riga["codice"], riga["ora_inizio"], riga["ora_fine"], cursor)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    aggiorna_tutte_le_righe()
    print("Ore di sonno aggiornate.")
