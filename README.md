# PracticaDjango

##  ------------ Introduccion ----------------
1. Hemos configurado el entorno virtual en Anaconda
    ==> conda create -n (nombre_del_entono) python=(Version Python)

2. Hemos instalado Django y Pillow usando PiP(administrador de paquetes)
    - Ver la version de django 
        import django
        django.get_version()

3. Hemos creado el espacio de entrono de trabajo en GitHub
    A. luego lo conetamos con VSCode

4. Configurar el proyecto. Creando el Proyecto : 

     - -  django-admin startproject proyecto1 . (punto al final para que no cree mas carpets)
     - Configuramos el settigs.py 
        - TIME ZONE 
        - LANGUAGE_CODE : 'es_ES'
        - STATIC_URL = 'static/'
        - STATIC_ROOT = 'static'


5. Configurar la base de datos 
    Hacer las migraciones para conectar con la base de datos 
    Las migraciones es la manera como Django aplica los cambios que hace a sus modelos (agregando un campo, eliminando un modelo, etc.) en su esquema de base de datos

    - - python manage.py migrate

    Hay varios comandos que usará para interactuar con las migraciones y el manejo de Django del esquema de la base de datos:
    - migrate.- Que es responsable de aplicar y dejar de aplicar las migraciones. 

    - makemigrations.- Que es responsable de crear nuevas migraciones basadas en los cambios que ha realizado en sus modelos.

    - sqlmigrate.- Que muestra las declaraciones de SQL para una migración.

    - showmigrations.- Que enumera las migraciones de un proyecto y su estado.

6. Plugin de SQLite que uso en VS Code :
     https://github.com/AlexCovizzi/vscode-sqlite/?tab=readme-ov-file


7. Crear un superusuario para el manejo de la admin

    - Nombre : ela
    - Password : 123456789

8. Creamos las carpetas con las que vamos a trabajar 

    - - Dentro de la carpeta Roots que es : DJ_PRACTICA
        - Media : Archivos subidos por el usuario

    - - Fuera de la carpeta Root que es : DJ_PRACTICA
        - Static : Contendra el js, css e imagenes 
        - Templates : Contendra las plantillas del proyecto

9. Creamos nuestra primera APPLICACION

    - - para crear la aplicacion dentro de la carpeta  apps
        - Primero accedemos a apps con cd apps
        - luego creamos la app dentro


    - Creado el aplicacion esta ves la llamaremos Blog
        - =>  : python manage.py startapp Blog
        - ...  nombre carpeta/nombre 

    - __init__.py.- Indica a Python que considere una carpeta como un módulo o también llamado paquete. 

    - admin.py.- Se realizan todos los cambios en la administración.

    - apps.py.- Proporciona un lugar para cualquier configuración específica de la aplicación.

    - models.py.- Es donde tendremos que crear todos nuestros modelos referidos a nuestra app.

10. Configuramos la aplicacion que acabamos de creear en este caso : Blog 

    - En el settings.py del proyecto (proyecto1)
    - En INSTALLED_APPS poner la ubicacion del archivo 
        - - poner sole blog o redirigirlo con 'blog.apps.BlogConfig'

11. Crear el modelo del Post  en blog/models

    - Escribiendo la clase donde se almacenara todas las tablas que vamos a usar en enste caso se llama :
        - Class Post()

    - luego creamos las tablas con 
        - - python manage.py makemigrations blog
        -- python manage.py migrate blog  