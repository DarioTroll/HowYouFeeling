import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, time

# Carica variabili ambiente
load_dotenv()

def calcola_ore_sonno(ora_inizio, ora_fine) -> float:
    formato = "%H:%M:%S"

    def to_str(ora, label):
        if isinstance(ora, time):
            return ora.strftime(formato)
        elif isinstance(ora, timedelta):
            # Converti timedelta in HH:MM:SS
            total_seconds = int(ora.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        elif isinstance(ora, str):
            return ora
        else:
            raise TypeError(f"{label} deve essere una stringa, time o timedelta (hai {type(ora)})")

    try:
        ora_inizio_str = to_str(ora_inizio, "ora_inizio")
        ora_fine_str = to_str(ora_fine, "ora_fine")

        start = datetime.strptime(ora_inizio_str, formato)
        end = datetime.strptime(ora_fine_str, formato)

        if end <= start:
            end += timedelta(days=1)

        durata = end - start
        return round(durata.total_seconds() / 3600, 2)
    except Exception as e:
        print(f"[Errore] Calcolo ore fallito per valori: ora_inizio={ora_inizio}, ora_fine={ora_fine} -> {e}")
        return 0.0

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
