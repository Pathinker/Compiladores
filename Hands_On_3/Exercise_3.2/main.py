import sys
import os
import threading
import time

sys.path.append(os.path.join(os.path.dirname(__file__), 'compiler'))

from compiler.lexer import lexer
from compiler.parser import parser

inactividad = 0
tiempo_limite = 30
activo = True

def contador_inactividad():
    global inactividad, activo
    while activo:
        time.sleep(1)
        inactividad += 1
        if inactividad >= tiempo_limite:
            print("\n30 segundos sin actividad. Saliendo...")
            os._exit(0)

hilo_contador = threading.Thread(target=contador_inactividad, daemon=True)
hilo_contador.start()

while True:
    try:
        s = input("Ingresa una expresión: ")
        inactividad = 0 
    except EOFError:
        break
    if not s.strip():
        continue
    parser.parse(s + '\n')