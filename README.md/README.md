# 🌡️ Sistema de Monitoreo IoT con Arduino y Python

Proyecto de ejemplo que mide temperatura y humedad con un sensor DHT11 en Arduino, envía los datos por serial y los guarda en una base de datos SQLite usando Python.

## 🚀 Objetivo
Simular una arquitectura de telemetría en tiempo real: captura → transmisión → almacenamiento → visualización básica.

## 🧩 Materiales
- Arduino Uno/Nano/Mega  
- Sensor DHT11 (o DHT22)  
- Cables jumper  
- PC con Arduino IDE y Python 3  
- Librerías: *DHT sensor library by Adafruit* (Arduino), pyserial, sqlite3 (Python)

## ⚙️ Funcionamiento
1. Arduino lee temperatura y humedad con el DHT11.  
2. Envía los datos por el puerto serial en el formato T:<temp>;H:<hum>.  
3. Un script de Python recibe las lecturas y las almacena en SQLite (iot_datos.db).  
4. (Opcional) Se pueden graficar y analizar.

## 📂 Estructura
Sistema_monitoreo_IoT/ ├─ Arduino/ │  └─ sensor_dth.ino ├─ Python/ │  └─ monitoreo_iot.py └─ README.md

## 🖥️ Arduino (resumen)
- Pin de datos del DHT11 en D2.  
- Baudrate: 9600.  
- Envío cada 2 s.

## 🐍 Python (resumen)
- Puerto serial: ajustar COM3 (Windows) o /dev/ttyUSB0 (Linux).  
- Crea tabla lecturas(temperatura, humedad, fecha_hora).  
- Inserta una fila por cada lectura recibida.

## 📊 Ejemplo de salida
[2025-11-12 18:25:42] Temperatura: 26.5°C | Humedad: 58.3% [2025-11-12 18:25:44] Temperatura: 26.6°C | Humedad: 58.1%

## 🧠 Tecnologías
Arduino IDE · Python 3 · SQLite · Sensor DHT11

## 👩‍💻 Autora
Fátima Graciela Chiñas Martínez – Villahermosa, Tabasco  
📧 fatimachinas3108@gmail.com · 📞 9932305610
