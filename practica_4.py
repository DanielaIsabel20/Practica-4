import requests

def obtener_precio_bitcoin():
    try:
        response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response_json=response.json()
        precio_bitcoin=response_json["bpi"]["USD"]["rate_float"]
        return precio_bitcoin
    except requests.RequestException:
        print('Error, no se pudo obtener el precio de Bitcoin')

def main1():
    try:
        n=int(input('Ingrese la cantidad de bitcoins que posee: '))
        return n
    except ValueError:
        print('No ingresó un número válido')
        return

from pyfiglet import Figlet
import random
def main2(nombre_fuente):
    figlet=Figlet()
    fuentes_disponibles=figlet.getFonts()

    if nombre_fuente is None:
        fuente_utilizada=random(fuentes_disponibles)
    elif nombre_fuente in fuentes_disponibles:
        fuente_utilizada=nombre_fuente
    else:
        print('No se dispone de dicha fuente')
        return

    figlet.setFont(font=fuente_utilizada)
    texto_a_imprimir=input("Ingrese el texto que desea imprimir: ")
    texto_convertido=figlet.renderText(texto_a_imprimir)
    print(texto_convertido)

def guardar_tabla(numero):
    if numero<1 or numero>10:
        print('El número no está en el intervalo solicitado')
        return
    
    with open("Tabla-{}.txt".format(numero),"w") as file:
        for i in range(1,11):
            multiplicacion=numero*i
            line="{} x {}={}\n".format(numero,i,multiplicacion)
            file.write(line)

def mostrar_tabla(numero):
    try:
        with open("Tabla-{}.txt".format(numero),"r") as file:
            tabla=file.read()
            print(tabla)
    except FileNotFoundError:
        print('El archivo no existe')

def mostrar_linea(numero,linea):
    try:
        with open("Tabla-{}.txt".format(numero),"r") as file:
            lines=file.readlines()
            if linea<=0 or linea>len(lines):
                print('No existe la linea solicitada')
            else:
                print(lines[linea-1])
    except FileNotFoundError:
        print('El archivo no existe')

def main4():
    while True:    
        opc=input('Ingrese una opción: ')
        if opc=="1":
            numero_ingresado=int(input('Ingrese un número del 1 al 10: '))
            guardar_tabla(numero_ingresado)
        elif opc=="2":
            numero_ingresado=int(input('Ingrese un número del 1 al 10: '))
            mostrar_tabla(numero_ingresado)
        elif opc=="3":
            numero_ingresado=int(input('Ingrese un número del 1 al 10: '))
            linea_deseada=int(input('Ingrese la línea que desea visualizar: '))
            mostrar_linea(numero_ingresado,linea_deseada)
        elif opc=="4":
            print('HASTA LUEGO')
            break
        else:
            print('No ingresó una opción correcta, vuelva a intentarlo')

import requests
import csv

def guardar_precios_bitcoin_txt(precio):
    with open("precio_bitcoin.txt","w") as file:
        file.write(str(precio))

def guardar_precios_bitcoin_en_csv(precio):
    with open("precio_bitcoin.csv","w") as file:
        escribir_csv=csv.writer(file)
        escribir_csv.writerow(["Precio"])
        escribir_csv.writerow([precio])

def main5():
    precio_bitcoin5=obtener_precio_bitcoin()
    guardar_precios_bitcoin_txt(precio_bitcoin5)
    guardar_precios_bitcoin_en_csv(precio_bitcoin5)
    print("El precio de bitcoin es: {} USD".format(precio_bitcoin5))

import requests
import sqlite3
from datetime import datetime
def obtener_bitcoin_monedas():
    try:
        response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response_json=response.json()
        precios_bitcoin={
            "USD": response_json["bpi"]["USD"]["rate_float"],
            "GBP":response_json["bpi"]["GBP"]["rate_float"],
            "EUR":response_json["bpi"]["EUR"]["rate_float"]
        }
        return precios_bitcoin
    except requests.RequestException:
        print('Error, no se pudo obtener el precio de Bitcoin')

def base_de_datos_crypto():
    conectar=sqlite3.connect("cryptos.db")
    cursor=conectar.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bitcoin (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   precio_usd REAL,
                   precio_gbp REAL,
                   precio_eur REAL
                   )
''')
    conectar.commit()
    conectar.close()

def introducir_precios_bitcoin(cryptos):
    conectar=sqlite3.connect("cryptos.db")
    cursor=conectar.cursor()
    cursor.execute('''
        INSERT INTO bitcoin (precio_usd, precio_gbp, precio_eur)
        VALUES  (?,?,?)
    ''',(cryptos["USD"],cryptos["DBP"],cryptos["EUR"]))
    conectar.commit()
    conectar.close()

def main6():
    precios_bitcoin=obtener_bitcoin_monedas()
    base_de_datos_crypto()
    introducir_precios_bitcoin()
    print("Base de datos creada")

#problema 1: Bitcoin
print("----Ejercicio 1----")
numero_bitcoin=main1()
precio_bitcoin=obtener_precio_bitcoin()
valor_total_usd=numero_bitcoin*precio_bitcoin
formato_valor=f"${valor_total_usd:,.4f}"
print("El costo actual de {} Bitcoins es {}".format(numero_bitcoin,formato_valor))

#problema 2: letras grandes
print("----Ejercicio 2----")
nombre_ingresado=input('Ingrese el nombre de la fuente a utilizar: ')
main2(nombre_ingresado)

#problema 3: descargar imagenes
print("----Ejercicio 3----")
import requests
url="https://unsplash.com/es/fotos/9LkqymZFLrE"
response=requests.get(url)

with open('perrito_tierno.jpg','wb') as f:
    f.write(response.content)
    pass

print('Se guardó la imagen')

#problema 4: 
print("----Ejercicio 4----")
print('MENÚ')
print('Eliga una opción\n1)Guardar la tabla de multiplicar de un número\n2)Mostrar tabla de multiplicar\n3)Mostrar una linea de la tabla\n4)Salir\n')
main4()
#problema 5: crear doc para bitcoin
print("----Ejercicio 5----")
main5()

#problema 6: cryptos
print("----Ejercicio 6----")
main6()
