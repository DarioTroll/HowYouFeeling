import subprocess
import psutil
import os
import webbrowser
import time

# Configura i percorsi
paths = {
    "duc": r"C:\\Program Files (x86)\\No-IP\\duc40.exe",
    "nginx": r"C:\\nginx-1.28.0\\nginx-1.28.0\\nginx.exe",
    "nginx_dir": r"C:\\nginx-1.28.0\\nginx-1.28.0",
    "app_py": r"C:\\Users\\Dario\\Desktop\\Progetti\\Health\\app.py",
    "app_dir": r"C:\\Users\\Dario\\Desktop\\Progetti\\Health"
}

def is_running(process_name, script_check=None):
    for proc in psutil.process_iter(['name', 'cmdline']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                if script_check and script_check.lower() not in ' '.join(proc.info['cmdline']).lower():
                    continue
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

def start_duc():
    if not is_running("duc.exe"):
        print("Avvio DUC...")
        subprocess.Popen([paths["duc"]])
    else:
        print("DUC è già attivo.")

def start_nginx():
    if not is_running("nginx.exe"):
        print("Avvio NGINX...")
        subprocess.Popen([paths["nginx"]], cwd=paths["nginx_dir"])
    else:
        print("NGINX è già attivo.")

def start_app():
    if not is_running("python.exe", "app.py"):
        subprocess.Popen(
            ["pythonw", "app.py"],
            cwd=paths["app_dir"],
            creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
        )

def open_browser():
    print("Apro il browser su https://dariotrollo.ddns.net ...")
    webbrowser.open("https://dariotrollo.ddns.net")

if __name__ == "__main__":
    print("=== Avvio automatico servizi ===")
    start_duc()
    start_nginx()
    start_app()
    time.sleep(3)
    open_browser()
