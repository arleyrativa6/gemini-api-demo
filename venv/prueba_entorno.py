import requests 
import sys
import os

def verificar_configuracion():
    print("verificado")

    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("entorno virtual detectado")
    else:
        print("no se detecto entorno virtual")
    try:
        respuesta = requests.get("https//www.google.com")
        if respuesta.status_code == 200:
            print("conexion a internet verificada")
    except requests.RequestException as e:
        print("error al verificar conexion")

if __name__ == "__main__":
    verificar_configuracion()
