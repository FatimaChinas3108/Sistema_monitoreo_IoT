import serial
import sqlite3
import time

# Cambia 'COM3' por el puerto donde esté tu Arduino
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

# Crear la base de datos si no existe
conn = sqlite3.connect('iot_datos.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS lecturas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperatura REAL,
        humedad REAL,
        fecha_hora TEXT
    )
''')

print("Iniciando monitoreo...\n")

while True:
    datos = arduino.readline().decode('utf-8').strip()
    if datos.startswith("T:"):
        partes = datos.replace("T:", "").replace("H:", "").split(";")
        temperatura = float(partes[0])
        humedad = float(partes[1])
        fecha = time.strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("INSERT INTO lecturas (temperatura, humedad, fecha_hora) VALUES (?, ?, ?)",
                       (temperatura, humedad, fecha))
        conn.commit()

        print(f"[{fecha}] Temperatura: {temperatura}°C | Humedad: {humedad}%")