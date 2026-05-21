# Documentación Tecnica - PhysioScanWeb
A continuación se presenta la documentación tecnica correspondiente al proyecto PhysioScanWeb, desarrollado a lo largo de 5 sesiones.

## Entorno Virtual (Linux Mint)
Para sistemas basados en GNU/Linux debemos hacer uso de la herramienta *UV*, esta nos permite crear entornos virtuales con diferentes versiones de Python sin la necesidad de intalar Python en nuestro sistema global.
~~~sh
uv venv --python 3.11 # Se creara una carpeta .venv
# Ahora activamos nuestro entorno
source .venv/bin/activate
# (PhysioScanWeb) user@mypc:
~~~
## Instalación de Librerias
Usaremos *uv* para instalar las librerias que necesitamos.
~~~sh
uv pip install -r requirements.txt
# Las librerias que necesitamos son:
# mediapipe==0.10.14
# opencv-python==4.13.0.92
# streamlit==1.57.0
# numpy
~~~
> El archivo *requirements.txt* contiene todas las librerias que necesitamos

