# PracticaDjango

##  ------------ NOTAS  ----------------

1.  !Importante 
    
    El último parámetro, que se ve así en views.py : 

    - {} es un lugar en el que podemos agregar algunas cosas para que la plantilla las use.
        - - return render (request, 'blog/post_list.html', {})

        -- Necesitamos nombrarlos (los seguiremos llamando 'posts' por ahora). Se debería ver así: {'posts': posts}. 
            - - la parte antes de : es una cadena; tienes que envolverla con comillas: "Fíjate

2. REQUEST : Todo lo que recibimos del usuario via internet 




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


## ------------ Panel de Administracion ---------------

1. Para agretar , editar y borrar los los post que hemos modelado, usaremos el panel de administracion (admin) de django. 
    - En el fichero blog/admin.py tengo que registrar el modelo POST que acabamos de crear 

        - from .models import Post

        - admin.site.register(Post)

    - Con estas 2 linas lo registramos


2. Crear un superusuario para el manejo de la admin

    - python manage.py createsuperuser

    - Nombre : ela
    - Password : 123456789


3. Luego ir a /admin y Crear , editar la informacion post o informacion de la base de datos 

## ------------ Despliegar ---------------

#### --- Github ---

Es un capitulo que te ensena a despliegar tu pagina web en internet

1. utiliar para sabe que archivos vamos a subir siempre.

    - Git Status 
    - Git Add 
        - git add --all
    - git commit -m " PARTE 2: A... " 

#### --- Pythonanywhere ---

https://tutorial.djangogirls.org/es/deploy/

PythonAnywhere es un servicio para ejecutar código Python en servidores "en la nube".

1. Creamos la cuenta en pythonanywhere 

2. Creamos un API Token 

3. Volvemos al dashboard y y creamos una nueva consola con $Bash

Para desplegar una aplicación web en PythonAnywhere necesitas descargar tu código de GitHub y configurar PythonAnywhere para que lo reconozca y lo sirva como una aplicación web. Hay

<!-- 
        NO FUNCIONA 

4.  en la console de pythonanywhere lanzamos el comando 

- pip3.6 install --user pythonanywhere -->

5. Ejecuatamos el asistente para configuar automaticamete nuestra aplicacion desde Github

    - Para crear todo a la vez : 

        - $ pa_autoconfigure_django.py --python=3.6 https://github.com/"mi_nombre_de_github/repositorio".git

        - En este caso : nombre de repositorio el github Clone HTTPS
        - https://github.com/LinoELa/PracticaDjango.git

        - EN ESTE CASO HE UTILIZADO : 

        - $ pa_autoconfigure_django.py --python=3.6 https://github.com/LinoELa/PracticaDjango.git


6. Creamos un superusuario 
    - python manage.py createsuperuser
        - ela098
        -Python@098

    - puedo ver mi codigo con la linea de comandos con :
        - ls 
        - ls blog/ (o la carpeta que quiera ver )


7. Para actualizar despues de haber subido o actualizado el proyecto el GitHub

    URL : al final de la pagina esta la informacion

    https://tutorial.djangogirls.org/es/html/

    A. GitHub
    
    - - Hacer un commit 
        - git status 
        - git add --all 
        - git status 
        - git commit -m 'nombre del commit'
        - git push 

    B. Revision 
        - Revistar si en settigs.py he puesto la url en : (en este caso : )
            - - ALLOWED_HOSTS = ['ela098.pythonanywhere.com']
        - Quitar la basede datos  la GitIgnore para que no ignore la base de datos.

    B. Python Any Where

    - - Abrir la pagina de Python Any where 
    - Ir a la consola o empezar una nueva 
        - - si voy a empezar una nueva puedo reactivar el enviroment con:
            - $  workon <nombre-domonio> 
                - workon ela098.pythonanywhere.com

    - Luego ir al archivo siguiente 
        - $ cd ~/<your-pythonanywhere-domain>.pythonanywhere.com
        - git pull (SI NO FUNCIONA )
        -git pull git pull origin main

    - Luego ir a mi inicio y pulsar Webs, despues. 
        - Pulsar RELOAD


8. Nombre y Password de la /admin
    -  Al poner el ALLOWED_HOSTS y subirlo a produccion pues 
    - Nombre y Password se  convierten en el mismo que yo uso en local
        - En este caso
            - ela
            - 123456789
    - ALLOWED_HOSTS = ['ela098.pythonanywhere.com']
    
## ------------ URLs  ---------------

https://tutorial.djangogirls.org/es/django_urls/

CUna URL es una dirección de la web. 
Cada página en Internet necesita su propia URL. De esta manera tu aplicación sabe lo que debe mostrar a un usuario que abre una URL. 

En Django utilizamos algo que se llama URLconf (configuración de URL). URLconf es un conjunto de patrones que Django intentará comparar con la URL recibida para encontrar la vista correcta.



1. Configuramos urls 
    - importando include  desde django.urls
    - luego ponemos el path ('' , incluede () ) para la direccion principal


2. Creamos un nuevo fichero urls.py en la carpeta blog  pero podemos crear templates primero

    Dentro del nuevo fichero importamos path y los vies 
    - from django.urls import path
    - from . import views

    - luego creamos nuestro propio url patterns y lo configuramos

## ------------ VISTAS  ---------------

https://tutorial.djangogirls.org/es/django_views/

Una ViewS.py es un lugar donde ponemos la "lógica" de nuestra aplicación.

Pedirá información del modelo que has creado antes y se la pasará a la plantilla.

    - creamos nuestra primera funcion para la vista 


## ------------ HTML : PLANTILLAS   ---------------

https://tutorial.djangogirls.org/es/html/


Una plantilla es un archivo que podemos reutilizar para presentar información diferente de forma consistente

Las plantillas se guardan en el directorio de blog/templates/blog. Así que primero crea un directorio llamado templates dentro de tu directorio blog. Luego crea otro directorio llamado blog dentro de tu directorio de templates:

blog
└───templates
    └───blog

1. (Tal vez te estés preguntando por qué necesitamos dos directorios llamados blog – como verás más adelante, es una convención de nombres que nos facilitará la vida cuando las cosas se pongan más complicadas.)

2. Y ahora crea un archivo post_list.html (déjalo en blanco por ahora) dentro de la carpeta blog/templates/blog.

    - Aunque se veea en blanco es la forma corecta 
    - Si nada error pues reiniciar el servidor 

3. Ahora podemos editar el archivo post_list.html que hemos creado
    - poniendo la estrucuta basica de un HTML 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Ola's Blog </title>
</head>
<body>

<!-- ... -->
    
</body>
</html>


4. PERSONALIZAMOS LA PLANTILLA 

    Pero una personalizar basica 




## ------------ BBDD & QuerySet  ---------------

https://tutorial.djangogirls.org/es/django_orm/

Un QuerySet es, en esencia, una lista de objetos de un modelo determinado. Un QuerySet te permite leer los datos de la base de datos, filtrarlos y ordenarlos.


1. Abrimos la consola shell de VSCode 
    -  python manage.py shell
    - Ahora estás en la consola interactiva de Django. Es como una consola de Python normal, pero con un poco de magia de Django. :) Aquí también se pueden usar todos los comandos de Python.

2. Todos los objetos 
   - Para ver los los Post que tenemos en la base de datos hacemos 
        - from blog.models import Post
        - Post.objects.all()
3. Crear Objetos 
    - Vamos a crear nuevos objetos Post enla base de datos desde el Command Lines 

        - from django.contrib.auth.models import User 
        - me = User.objects.get(username = 'ela')
        - Post.objects.create(autor = me , title = 'Proyecto desde Comandos ', text = 'Test')
        - Para probar si esta bien 
            - Post.objects.all()
        - Publicar 
            - post = Post.objects.get(title = 'Proyecto desde Comandos')
            - post.publish()

    - Con esto se agregar nuevas entradas post desde la linea de comandos 


4. Filtar Objetos 
    Una parte importante de los QuerySets es la habilidad para filtrar los resultados. Digamos que queremos encontrar todos los post del usuario ola. Usaremos filter en vez de all en Post.objects.all(). Entre paréntesis estableceremos qué condición (o condiciones) debe cumplir un post del blog para aparecer como resultado en nuestro queryset. En nuestro caso sería author es igual a me. 

    - Ver todas las entradas de un usuario 
        - - Post.objects.filter(autor = me )

    - Ver las entradas que contengan la palabra 'title'
        - - Post.objects.filter(title__contains='title')


5. Ordenar Objetos 
    Los QuerySets también te permiten ordenar la lista de objetos.

    -Ordenar de forma normas 
        - Post.objects.order_by('create_date')
    - Invertir el orden
        - Post.objects.order_by('-create_date')

6. Consultas complejas y Combinacion de consultas 

    Como ves, algunos métodos en Post.objects devuelven un QuerySet. Los mismos métodos pueden ser llamados también en un QuerySet, y entonces devolverán un nuevo QuerySet. También puedes combinar QuerySets encadenando uno con otro:

    - fron django.utils import timezone 
    - Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')



7. Para salir seria 

    - exit()


## ------------ DATOS DINAMICOS EN PLANTILLAS  ---------------

!Importante 

https://tutorial.djangogirls.org/es/dynamic_data_in_templates/

Tenemos diferentes piezas en su lugar: el modelo Post está definido en models.py, tenemos a post_list en views.py y la plantilla agregada. ¿Pero cómo haremos realmente para que nuestros posts aparezcan en nuestra plantilla HTML?

Esto es exactamente lo que las views se supone que hacen:
    - Conectar modelos con plantillas.
    - En nuestra view post_list necesitaremos tomar los modelos que deseamos mostrar y pasarlos a una plantilla.
    - En una vista decidimos qué (modelo) se mostrará en una plantilla.
    - Ahora tenemos que incluir el modelo que definimos en el archivo models.py. Agregaremos la línea from .models import Post 
        - 



## ------------ PLANTILLAS DE DJANGO  ---------------

https://tutorial.djangogirls.org/es/django_templates/


1. Etiquetas de plantilla 

    HTML no se puede escribir código en Python porque los navegadores no lo entienden. Sólo saben HTML. Sabemos que HTML es bastante estático, mientras que Python es mucho más dinámico.
    Las etiquetas de plantilla de Django nos permiten insertar elementos de Python dentro del HTML, para que puedas construir sitios web dinámicos más rápida y fácilmente.

2. Mostrar la plantilla lista de POSTS
    En datos dinamico dimos a nuestra plantilla una lista de entradas en la variable posts. Ahora la vamos a mostrar en HTML.


    Para imprimir una variable en una plantilla de Django, utilizamos llaves dobles con el nombre de la variable dentro, algo así:

    - blog/templates/blog/post_list.html
            - - {{ posts }}

    - HTML, para ver lo si ya funcionado y trae la informacion de la base de datos, se puede usar dentro del archivo .html

        - - {% comment %} {{ posts }} {% endcomment %}

    - ¿Recuerdas de Introducción a Python cómo podemos mostrar listas? Sí, ¡con bucles for! En una plantilla de Django se hacen así:

         - - {% for post in posts %} {{ post }}{% endfor %}



    Todo lo que pongas entre {% for %} y {% endfor %} se repetirá para cada objeto de la lista. Refresca la página:

    - ({{ post.title }} o {{ post.text }})? Estamos accediendo a los datos en cada uno de los campos definidos en nuestro modelo Post. También el |linebreaksbr está pasando el texto de los post a través de un filtro para convertir saltos de línea en párrafos.





## ------------ CSS ---------------

https://tutorial.djangogirls.org/es/css/

- https://getbootstrap.com/

    - Vamos a utilizar Boostrap que es un frameworks dee HTML y CSS, Lo escribieron programadores que trabajaban en Twitter. ¡Ahora lo mantienen y desarrollan voluntarios de todo el mundo.
    - Instalar 
        - En la Head de HTML  poner : o mirar las nuevas versiones 

        - link web : https://bootstrapdocs.com/v3.3.0/docs/getting-started/

        - Se llaman : CDN  

            - <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css">
            - <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap-theme.min.css">
            - <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">


-  (STATIC FILES ) Archivos Estaticos 

    - Los archivos estáticos son los archivos CSS e imágenes. Su contenido no depende del contexto de la petición y siempre será el mismo para todos los usuarios.
        - Donde poner los archivos ESTATICOS en Django , Django ya sabe dónde encontrar los archivos estáticos de la app "admin" con la referencia de :  [ aunque  otra gente usa  MEDIA. ]
            - STATIC_URL = 'static/'
            - STATIC_ROOT = BASE_DIR / 'static'.
        - Ahora necesitamos añadir los archivos estáticos de nuestra aplicación, blog.
        - Crearemos una carpeta llamada static dentro de la app blog:

djangogirls
├── blog
│   ├── migrations
│   ├── static
│   └── templates
└── mysite


- PRIMER ARCHVIO CSS
    - Crea un nuevo directorio llamado css dentro de la carpeta static
    - A continuación, crea un nuevo archivo llamado blog.css dentro de la carpeta css.
    djangogirls
        └─── blog
             └─── static
                  └─── css
                       └─── blog.css

    - Configurar el el blog.css : Agregar los estilos 
        - Para decirle a nuestra plantilla HTML que hemos anadido codigo CSS tenemos que abrir el archivo blog/templates/blog/post_list.html en el editor de código y añade la siguiente linea de codigo   al principio del todo: 

            - {% load static %}

        - luego decirle a la plantilla donde esta nuestra carpeta CSS 

            - <link rel="stylesheet" href="{% static 'css/blog.css' %}">

    - Luego editar el css y el HTML ponerle las clases y etiquetas para que se pueda llamar en CSS y funcione.
        

        






    





























