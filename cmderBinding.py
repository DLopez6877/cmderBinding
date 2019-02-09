import subprocess
import keyboard
import psutil
import os

keyboard.press_and_release('ctrl+`')
runningCmder = "ConEmu64.exe" in (p.name() for p in psutil.process_iter())
if not runningCmder:
    os.startfile('E:/Program Files (x86)/Cmder/Cmder.exe')