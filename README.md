
# PhysioScan Web
### Evaluador Postural Inteligente con Visión por Computadora

PhysioScan Web es una aplicación web desarrollada en Python que utiliza técnicas de visión artificial e inteligencia artificial para realizar análisis postural en tiempo real mediante una cámara web convencional.

El sistema implementa MediaPipe BlazePose para detectar automáticamente 33 puntos anatómicos del cuerpo humano y calcular métricas biomecánicas relacionadas con cuello, hombros y postura corporal, permitiendo visualizar información en tiempo real desde una interfaz web construida con Streamlit.

---

# Características Principales

- Detección de pose humana en tiempo real  
- Seguimiento corporal mediante 33 landmarks anatómicos  
- Cálculo automático de ángulos biomecánicos  
- Interfaz web interactiva con Streamlit  
- Renderizado visual del esqueleto corporal  
- Visualización de métricas posturales  
- Funcionamiento multiplataforma (Linux / Windows)  
- No requiere hardware especializado  
- Procesamiento completamente local  

---

# Tecnologías Utilizadas

| Tecnología | Función |
|---|---|
| Python 3.11 | Lenguaje principal |
| MediaPipe BlazePose | Detección corporal mediante IA |
| OpenCV | Captura y procesamiento de video |
| Streamlit | Interfaz web interactiva |
| NumPy | Operaciones matemáticas |
| Git & GitHub | Control de versiones |

---

# Arquitectura del Proyecto

```text
PhysioScanWeb/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   ├── logo/
│
├── docs/
│   ├── diagrams/
│   ├── reports/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── constants.py
│   ├── utils.py
│   │
│   ├── pose_detector.py
│   ├── processor.py
│   ├── geometry.py
│   ├── renderer.py
│   │
│   └── exercises.py
│
├── tests/
│   ├── test_geometry.py
│   ├── test_detector.py
│   └── test_processor.py
│
├── .env
└── .venv/
```

---

# Funcionamiento General

El flujo de funcionamiento del sistema es el siguiente:

1. La aplicación accede a la cámara web.
2. OpenCV captura cada frame de video.
3. MediaPipe BlazePose detecta los landmarks corporales.
4. El módulo geométrico calcula ángulos articulares.
5. El renderizador dibuja el esqueleto y las métricas.
6. Streamlit muestra los resultados en tiempo real.

---

# Métricas Biomecánicas Implementadas

Actualmente el sistema analiza:

- Inclinación cervical
- Elevación de hombros
- Postura de cabeza
- Alineación corporal básica

---

# Requisitos del Sistema

## Hardware
- Cámara web integrada o USB
- Procesador multinúcleo
- 8GB RAM recomendados

## Software
- Python 3.11
- Windows 10/11 o GNU/Linux

---

# Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/jeancorro137/PhysioScanWeb.git
```

---

## 2. Entrar al proyecto

```bash
cd PhysioScan-Web
```

---

## 3. Crear entorno virtual

## Entorno Virtual (Linux Debian)
Para sistemas basados en GNU/Linux debemos hacer uso de la herramienta *UV*, esta nos permite crear entornos virtuales con diferentes versiones de Python sin la necesidad de intalar Python en nuestro sistema global.
~~~sh
uv venv --python 3.11 # Se creara una carpeta .venv
# Ahora activamos nuestro entorno
source .venv/bin/activate
# (PhysioScanWeb) user@mypc:
~~~

### Entorno Virtual (Windows)
Para sistemas Windows debemos crear un entorno virtual mediante los siguiente comandos:
~~~sh
python -m venv .venv
pip install -r requirements.txt
~~~

### Instalación de Librerias
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

### Ejecución de modulos Python
Para ejecutar modulos independientes debemos seguir la siguiente estructura, para garantizar que el modulo ejecutado pueda comunicarse con los demas módulos:
~~~sh
#python -m paquete.modulo
python -m tests.test_pose # Por ejemplo
~~~

---

# Ejecución

Para iniciar la aplicación:

```bash
streamlit run app.py
```

Luego abrir en el navegador:

```text
http://localhost:8501
```
## Rendimiento
Para mejorar el rendimiento podemos modificar la resolución de la camara:
~~~py
self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #valor_numerico 320
self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #valor_numerico 240
~~~
---

# Motor de Inteligencia Artificial

El núcleo del proyecto utiliza MediaPipe BlazePose, un modelo optimizado de visión por computadora desarrollado por Google.

El sistema es capaz de:

- Detectar 33 puntos anatómicos
- Estimar postura corporal
- Procesar video en tiempo real
- Ejecutarse directamente en CPU

---

# Objetivo del Proyecto

El objetivo principal de PhysioScan Web es apoyar procesos de evaluación postural y fisioterapia mediante herramientas accesibles de inteligencia artificial, eliminando la necesidad de hardware especializado o sensores externos.

---

# Limitaciones

- No reemplaza diagnóstico médico profesional
- No utiliza calibración clínica certificada
- Requiere buena iluminación
- Puede perder precisión con oclusiones corporales

---

# Futuras Mejoras

- Historial de sesiones
- Exportación de resultados
- Base de datos de pacientes
- Aplicación móvil
- Modelos biomecánicos avanzados
- Integración con nube

---

# Autores

## Grupo de Desarrollo PhysioScan Web

- Jean Paul Corro T.
- Danna Jireth Diaz Polo
- Diana Sofia Rengifo

---

# Contexto Académico

Proyecto académico enfocado en:
- Visión Artificial
- Inteligencia Artificial
- Biomecánica
- Fisioterapia Digital
- Desarrollo Web

---

# Licencia

Proyecto académico desarrollado con fines educativos.

Uso libre para aprendizaje e investigación.

---

# Agradecimientos

- Google MediaPipe Team
- Comunidad OpenCV
- Streamlit
- Python Software Foundation
- Talento Tech
- Docentes de Talento Tech

