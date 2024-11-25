# Image Processing Web Application - Django

---

### Explicación de las Secciones:

1. **Introducción**: Resumen claro del propósito del proyecto y la funcionalidad principal.
2. **Instalación**: Detalles sobre cómo configurar el proyecto en tu entorno local, incluyendo la creación del entorno virtual y la instalación de dependencias.
3. **Configuración**: Configuración de la base de datos y los archivos multimedia.
4. **Ejecución**: Instrucciones para ejecutar el servidor de desarrollo.
5. **Uso de la aplicación**: Pasos para interactuar con la aplicación a través de la interfaz web.
6. **Archivos del Proyecto**: Mención de los archivos principales del proyecto (sin mostrar el código, para que los usuarios lo vean directamente en el repositorio).
7. **Contribuciones**.
8. **Licencia**: Mención de la licencia del proyecto.
9. **Agradecimientos**.

## Introducción

Este proyecto tiene como objetivo principal crear una **aplicación web en Django** que permita a los usuarios:

- **Subir imágenes**: Los usuarios pueden cargar imágenes desde sus dispositivos.
- **Procesar las imágenes**: La aplicación genera un mapa de calor (aunque en el código actual se genera una imagen vacía, en escenarios reales se podría procesar la imagen para crear un mapa de calor visual).
- **Generar reportes en PDF**: Después de procesar la imagen, se genera un reporte PDF con los datos del cliente y un enlace a la imagen procesada (por ejemplo, el mapa de calor generado).

### Funcionalidades clave

- **Carga de imágenes**: Los usuarios pueden cargar imágenes a través de un formulario.
- **Almacenamiento de imágenes y datos del cliente**: La aplicación almacena tanto los datos del cliente (nombre, correo electrónico, teléfono) como las imágenes subidas.
- **Generación de mapas de calor**: Aunque el código actual no implementa un procesamiento real, el objetivo es generar un mapa de calor de las imágenes subidas, lo cual se utiliza comúnmente en análisis de imágenes, visión computacional, entre otros.
- **Generación de reportes PDF**: Se genera un archivo PDF con los datos del cliente y la imagen procesada, el cual puede ser descargado.
- **Interfaz web**: La aplicación está accesible a través de un navegador, permitiendo a los usuarios interactuar con los formularios.

### Resumen

Es una **aplicación web** que permite a los usuarios:

1. Subir imágenes de su elección.
2. Procesarlas (por ejemplo, creando un mapa de calor).
3. Generar un **reporte en PDF** con los datos del cliente y la imagen procesada.

### Posibles aplicaciones

Este tipo de plataformas es útil en diversas áreas, tales como:

- **Análisis de imágenes**: Como imágenes médicas, científicas o visualización de datos espaciales.
- **Gestión de información de clientes**: Almacenar datos de contacto y realizar análisis o visualización de imágenes.
- **Generación de reportes automáticos**: Estos pueden ser descargados o enviados como archivos PDF.

---
## Instalación

### Requisitos previos

Asegúrate de tener **Python** y **Django** instalados en tu sistema. Además, necesitarás algunas dependencias adicionales para manejar imágenes y generar PDFs.

#### Instalar dependencias

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/imagen-processing-django.git
cd imagen-processing-django

```
2. Crea un entorno virtual y activa el entorno (opcional pero recomendado):

```bash
python -m venv venv

# En macOS/Linux:
source venv/bin/activate
```
3. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```
Este archivo **requirements.txt** debe contener los siguientes paquetes esenciales:
```bash
Django==4.x
opencv-python==4.x
numpy==1.x
weasyprint==52.x
```

---

## Configuración del Proyecto

1. Base de datos: Este proyecto usa SQLite por defecto. No es necesario hacer ninguna configuración adicional para usar SQLite, pero si quieres usar otro sistema de base de datos (como PostgreSQL o MySQL), tendrás que actualizar la configuración en **settings.py**.

2. Archivos estáticos y multimedia: El proyecto está configurado para servir archivos estáticos y archivos de medios (como las imágenes subidas y los reportes PDF generados) durante el desarrollo.

    Asegúrate de crear la carpeta **media/** en el directorio raíz de tu proyecto para almacenar las imágenes y los mapas de calor generados.

```bash
mkdir media
```

    También asegúrate de que tu carpeta static/ esté configurada correctamente, ya que allí se almacenarán los archivos estáticos como los archivos CSS personalizados.

```bash
mkdir static/css
```

3. Configuración de settings.py: Abre el archivo settings.py en el proyecto y agrega las siguientes líneas para asegurarte de que Django pueda manejar correctamente los archivos estáticos y multimedia:

```bash
# Archivos multimedia (para las imágenes y mapas de calor generados)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Archivos estáticos (CSS y demás archivos)
STATIC_URL = '/static/'

# Carpeta para archivos estáticos
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Asegura que Django encuentre la carpeta static
]
```

---
## Migrar la Base de Datos
Antes de ejecutar el servidor, realiza las migraciones para crear las tablas necesarias en la base de datos:

```bash
python manage.py migrate
```
---
## Ejecutar el Servidor de Desarrollo
Para ejecutar el servidor de desarrollo de Django:

```bash
python manage.py runserver
```
Esto iniciará el servidor en **http://127.0.0.1:8000/** (o la URL que se indique en la terminal).

---
## Uso de la Aplicación
1. Accede a la aplicación a través de tu navegador en **http://127.0.0.1:8000/**
2. Completa el formulario con los datos del cliente (nombre, correo electrónico, teléfono).
3. Carga la imagen desde tu dispositivo.
4. El sistema procesará la imagen y generará un mapa de calor (actualmente vacío).
5. El reporte se generará en formato PDF, incluyendo los datos del cliente y la imagen procesada (mapa de calor).

## Archivos del Proyecto
Puedes ver los detalles de los archivos en el repositorio para comprender la estructura del proyecto. A continuación, se describen los archivos principales del proyecto:

- **models.py**: Define los modelos de datos para la aplicación (cliente e imagen).
- **forms.py**: Define los formularios utilizados para cargar imágenes y recopilar la información del cliente.
- **views.py**: Maneja la lógica de las vistas, incluyendo la carga de imágenes, el procesamiento y la generación de PDFs.
- **index.html**: Plantilla HTML para el formulario de carga de imágenes y entrada de datos del cliente.
- **pdf_template.html**: Plantilla HTML para generar el reporte PDF con los datos y la imagen procesada.

---
## Contribuciones
Si deseas contribuir al proyecto, por favor sigue estos pasos:

- Haz un fork de este repositorio.
- Crea una nueva rama **(git checkout -b feature/nueva-funcionalidad)**.
- Realiza tus cambios.
- Haz commit de tus cambios **(git commit -am 'Agregada nueva funcionalidad')**.
- Haz push a la rama **(git push origin feature/nueva-funcionalidad)**.
- Abre un Pull Request.

---
## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

---
## Agradecimientos

Gracias por revisar este proyecto. ¡Espero que encuentres útil la aplicación! Si tienes alguna sugerencia o mejora, no dudes en abrir un issue o pull request.