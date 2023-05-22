# Blog de actividades

### Estructura

El blog está en un solo repositorio para que todos puedan probar el blog completo, pero está dividido en 2 partes:

- **Frontend**: La parte del cliente. Viene siendo el sitio en sí, el HTML, CSS y JavaScript. El cliente no interactúa directamente con una base de datos, sino que debe interactuar con un servidor.
- **Backend**: La parte del servidor. Aquí se utiliza una API REST, un servicio de intercambio de datos a través de rutas específicas. El cliente interactúa con la API, la cual interactúa con la base de datos.

# Requisitos

Antes de explicar la aplicación como tal, hay que mencionar las herramientas ideales.

### Git

Este proyecto utiliza **Git**, un sistema de control de versiones que permite que multiples personas trabajen en el mismo proyecto, evitando problemas como la sobreescritura y pérdida de información. Git puede descargarse desde [ésta pagina](https://git-scm.com/downloads).

Es una herramienta normalmente utilizada por consola, pero existen editores de código que nos permiten utilizar Git a través de la interfáz gráfica, como el que se menciona a continuación.

### Visual Studio Code

Visual Studio Code es un editor de código que sirve para muchos lenguajes de programación, y permite instalar extensiones para aumentar su funcionalidad. Tiene control de versiones integrado, por lo cual no hace falta memorizar y utilizar comandos de Git. Aún así no está de más aprender Git. Puede descargarse desde la [página oficial](https://code.visualstudio.com/).

Al instalar el editor, se recomienda instalar la extensión oficial de Python, ya que ésta detecta inmediatamente los entornos virtuales.

### Python

Todos los que quieran probar y trabajar en el blog deben instalar Python, pero no es necesario aprender el lenguaje. Python puede descargarse desde la [página oficial](https://www.python.org/).

# Instalación

Montar el proyecto al inicio requiere ejecutar muchos comandos, pero luego no hará falta. Solo se necesitará 3 comandos para ejecutar el proyecto cada vez que se desee.

### Clonando el repositorio

Una vez instalado todo, procedemos a montar el proyecto. Primero clonamos el repositorio con Git, y configuramos nuestros datos en el repositorio, de lo contrario no podemos subir cambios.

Abrimos la consola y en la carpeta donde querramos guardar el proyecto, ejecutamos los siguientes comandos. No cerraremos la consola, ya que aún faltan más comandos.

```txt
git clone https://github.com/unexca11211/blog
cd blog
git config user.name "Nombre y Apellido"
git config user.email "Correo Electrónico"
```

Esto crea una carpeta nueva con el repositorio, y algunos archivos ocultos que contienen la configuración del repositorio. Aún no abriremos la carpeta con el editor de código.

### Creando el entorno virtual

Para este proyecto se utiliza un entorno virtual de Python. De este modo instalamos librerías únicamente para el proyecto, en lugar de librerías globales.

Ejecutamos el siguiente comando:

```txt
python -m venv .venv
```

Una vez creado el entorno virtual, ya podemos abrir la carpeta con el editor de código, el cual detecta y carga el entorno virtual.

### Instalando las librerías

Dentro del editor de código, podemos abrir terminales directamente sobre la carpeta que se esté trabajando. En Windows, Visual Studio Code abre por defecto terminales PowerShell.

Ejecutamos los siguientes comandos:

```txt
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

El primer comando permite ejecutar scripts, el segundo comando activa el entorno virtual en la terminal, y el último instala las librerías especificadas en el archivo de requisitos.

### Ejecutando el proyecto

Por último, podemos arrancar el proyecto con los siguientes comandos:

```txt
$env:FLASK_DEBUG = "1"
flask run
```

Se habilita una ruta local para probar el blog completo, y el proyecto se reinicia cada vez que se actualice un archivo, así no tenemos que reiniciar el proyecto manualmente a cada rato. La ruta por defecto debería ser http://localhost:5000/

# La aplicación en detalle

### Flask

El blog de actividades utiliza Flask, un framework que permite crear páginas web completas. Flask tiene una documentación excelente en su [página oficial](https://flask.palletsprojects.com/), pero solo está disponible en Inglés.

Para éste proyecto se crearon 2 planos:

- **frontend**: Éste plano solo se encarga de mostrar los archivos HTML, CSS y JS en la carpeta `frontend/web`.
- **backend**: El plano de la API.

El plano **frontend** apunta a la raíz, es decir, con solo entrar a la ruta del proyecto ya abrimos el HTML, CSS y JS. El plano **backend**, en cambio, apunta a `/api`.

Aquellos que desarrollen la parte **frontend** directamente trabajan sobre la carpeta `frontend/web`, no hace falta tocar el código de Python a menos que quieran contribuir.

Los desarrolladores de la parte **backend**, trabajan principalmente el plano **backend**, pero pueden tocar todo el proyecto si es necesario.

### SQLAlchemy

SQLAlchemy es una librería que simplifica trabajar con bases de datos. En lugar de escribir SQL, se trabaja con objetos que representan las tablas de las bases de datos. Tambíen tiene [documentación oficial](https://docs.sqlalchemy.org/en/20/index.html), aunque solo en Inglés. Principalmente importa aprender el modelo de relación de objetos (**ORM**).

### SQLite

SQLite es una base de datos sumamente sencilla, ya que directamente trabaja con archivos, y no requiere servicios pesados como el resto de las bases de datos.

SQLAlchemy permite trabajar con SQLite, por lo que no hace falta instalar programas adicionales. Pero siempre puede instalarse un programa para explorar bases de datos, y practicar con ellas.