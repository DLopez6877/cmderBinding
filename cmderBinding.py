import subprocess
import keyboard
import psutil


cmderIsRunning = "ConEmu64.exe" in (p.name() for p in psutil.process_iter())

if cmderIsRunning:
    keyboard.press_and_release('ctrl+`')
else:
    command = r"C:\Program Files (x86)\Cmder.exe"
    subprocess.call([command, '/c'])