@echo off

REM Navega até mosquitto
cd C:\Program Files\mosquitto

REM Inicia brooker mosquitto 
start mosquitto.exe -p 8080 -v 
timeout /T 2 /NOBREAK

REM Navegar para o diretório do projeto Django
cd C:\git\api_dispositivo\geotrack

REM Inicia receptor de coordenadas
start python C:\git\api_dispositivo\geotrack\dispositivo\start_mqtt.py
REM timeout /T 2 /NOBREAK

REM Ativar o ambiente virtual
REM call venv\Scripts\activate

REM Iniciar o servidor Django
REM python manage.py runserver --noreload

REM Inicia disparos de coordenadas mock
REM cd C:\git\pysquitto
REM timeout /T 1 /NOBREAK
REM start cmd /k python pub_pysquitto.py


