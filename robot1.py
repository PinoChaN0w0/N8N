import os
import sys
import json
import time
import glob
import shutil
import tempfile
import subprocess
import ctypes
import pyautogui
import pygetwindow as gw

# --- LOGGING SEPARADO ---
def log(msg):
    sys.stderr.write(f"[{time.strftime('%H:%M:%S')}] {msg}\n")
    sys.stderr.flush()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_PBIX = os.path.join(BASE_DIR, "Reporte.pbix")
NOMBRE_PDF = "Reporte.pdf"
RUTA_PDF = os.path.join(BASE_DIR, NOMBRE_PDF)

user32 = ctypes.windll.user32

  # 1. Abrir Power BI Desktop
log(f"Abriendo Power BI con: {RUTA_PBIX}...")
try:
    os.startfile(RUTA_PBIX)
except Exception:
    subprocess.Popen(["cmd", "/c", "start", "", RUTA_PBIX], shell=True)

time.sleep(12)
 # Clics sobre el menú (Ventana maximizada)
pyautogui.click(84, 410)
time.sleep(1.5)
pyautogui.click(322, 222)