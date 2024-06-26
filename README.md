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

        - $ pa_autoconfigure_django.py --python=3.10 https://github.com/"mi_nombre_de_github/repositorio".git

        - En este caso : nombre de repositorio el github Clone HTTPS
        - https://github.com/LinoELa/PracticaDjango.git

        - EN ESTE CASO HE UTILIZADO : 
            - $ pa_autoconfigure_django.py --python=3.10 https://github.com/LinoELa/PracticaDjango.git


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
        - Quitar la base de datos  la GitIgnore para que no ignore la base de datos.

    B. Python Any Where

    - - Abrir la pagina de Python Any where 
    - Ir a la consola o empezar una nueva 
        - - si voy a empezar una nueva puedo reactivar el enviroment con:
            - $  workon <nombre-domonio> 
                - workon ela098.pythonanywhere.com

    - Luego ir al archivo siguiente 
        - $ cd ~/<your-pythonanywhere-domain>.pythonanywhere.com
        - git pull (SI NO FUNCIONA )
        -git pull origin main

    - Luego ir a mi inicio y pulsar Webs, despues. 
        - Pulsar RELOAD

    C. Para que el CSS funcione tengo que agregar los path donde estan el HTML y el queesta en CSS
        - En la imagan de abajo esta la donde agregarlo y como agregarlo 
        - Mejor lo pongo tambien a la carpeta 

    - ![alt text](image.png)

    D. Otra solicion para actualizar ser
    - si cambiamos nuestros ficheros CSS, tenemos que ejecutar un comando extra en el servidor para decirle que los actualice. Este comando se llama collectstatic.
        - activamos el vistual env  
            - workon <your-pythonanywhere-domain>.pythonanywhere.com
            - git pull 
            - python manage.py collectstatic

    E. Para actualizar puedo borrar todos los datos que estan dentro de la carpeta que he subido  desde github en esta caso (practicaDjango)
    
    - Luego hago :
    - pa_autoconfigure_django.py --python=3.10 https://github.com/LinoELa/PracticaDjango.git





8. Nombre y Password de la /admin
    -  Al poner el ALLOWED_HOSTS y subirlo a produccion pues 
    - Nombre y Password se  convierten en el mismo que yo uso en local
        - En este caso
            - ela
            - 123456789
    - ALLOWED_HOSTS = ['ela098.pythonanywhere.com']



9. SEGUN ELLOS UNA NUEVA DE POSTEAR SERIA 

- Primero subimos los archivo a GitHub
    - $ git status
    - $ git add --all .
    - $ git status
    - $ git commit -m "EL COMIR "
    - $ git push

- Luego en la consola de Bas de PythonAnyWhere
    - $ cd ~/<your-pythonanywhere-domain>.pythonanywhere.com
    - $ git pull
    - [...]

    
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
        

        


## -- EXTENDIENDO PLANTILLAS (Reutilizar Plantilla)  ---

la extensión de plantillas. Significa que puedes reutilizar partes del HTML para diferentes páginas del sitio web.
Las plantillas son útiles cuando quieres utilizar la misma información o el mismo diseño en más de un lugar. No tienes que repetirte a ti misma en cada archivo. Y

- CREAR UNA PLANTILLA BASE 
    Una plantilla base es la plantilla más básica que extiendes en cada página de tu sitio web.
    - Vamos a crear un archivo base.html en blog/templates/blog/:
blog
└───templates
    └───blog
            base.html
            post_list.html
-  copia todo el contenido de post_list.html en base.html
    - luego en base.html reemplaza por todo lo que hay en   <body> 
    - Despues insertar en contenido por un block content
        - {% block content %}
        - {% endblock %}

    -  ¡Acabas de crear un bloque! Hemos usado la etiqueta de plantilla {% block %} para crear un área en la que se insertará HTML. Ese HTML vendrá de otra plantilla que extiende esta (base.html).
    - Luego editar el post_list.html quitandole la contenido structural de HTML y dejando solo el de pytho en este caso seria 
    - Poner post_list.html dentro de un block content para decirle que es un contenido de block.

    {% extends 'blog/base.html' %}

    {% block content %}
        {% for post in posts  %}
            <div class='post'>
                <div class="date">
                    <p>Publicado : {{ post.published_date }}</p>
                </div>
                   <h2> <a href="">{{ post.title }}</a></h2>
                <p>{{ post.text | linebreaks}}</p>
            </div>
            {% endfor %}
    {% endblock %}

    - ¡Esto es lo que significa extender plantillas!

## ------------ EXTENDER LA APLICACION ---------------

https://tutorial.djangogirls.org/es/extend_your_application/


Ya hemos completado todos los diferentes pasos necesarios para la creación de nuestro sitio web

Sabemos cómo escribir un modelo, URL, vista y plantilla. También sabemos cómo hacer que nuestro sitio web sea bonito.


Vamos a crear una pagina para mostrar los  post 
a tenemos un modelo Post, así que no necesitamos añadir nada a models.py.

- CREAR UN ENLACE A LA PAGINA DE DETALLE DE UNA PUBLICACION
Insertamos esta direccion URL desde la etiqueta a 
    <h2> <a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h2>
    - La parte depost_detail significa que Django estará esperando un URL en blog/urls.py con el nombre=post_detail
    - pk=post.pk? pk se refiere a primary key (clave primaria),a cual es un nombre único por cada registro en una base de datos.
    -
    Debido a que no especificamos una llave primaria en nuestro modelo Post, Django creará una por nosotros (por defecto, un número que incrementa una unidad por cada registro, por ejemplo, 1, 2, 3) 


- CREAR UNA URL AL DETALLE DE UNA PUBLICACION

Vamos a crear una URL en urls.py para nuestra view post_detail!


- AGREGAR LA VISTA DE DETALLE DE LA PUBLICACION




    
## ------------ FORMULARIOS  ---------------

https://tutorial.djangogirls.org/es/django_forms/

https://docs.djangoproject.com/en/2.2/topics/forms/



Vamos a crear una forma agradable de agregar y editar posts en el blog.

El admin de Django está bien, pero es bastante difícil de personalizar y hacerlo bonito. Con forms tendremos un poder absoluto sobre nuestra interfaz; 

Lo bueno de los formularios de Django es que podemos definirlos desde cero o crear un ModelForm, el cual guardará el resultado del formulario en el modelo.

Como cada parte importante de Django, los formularios tienen su propio archivo: forms.py.

Necesitamos crear un archivo con este nombre en el directorio blog.

blog
   └── forms.py

Lo primero, necesitamos importar Django forms (from django import forms) y nuestro modelo Post (from .models import Post).

PostForm, como probablemente sospechas, es el nombre de nuestro formulario. Necesitamos decirle a Django que este formulario es un ModelForm (así Django hará algo de magia por nosotros) - forms.ModelForm es responsable de ello.

Luego, tenemos class Meta, donde le decimos a Django qué modelo debe ser utilizado para crear este formulario (model = Post).

Finalmente, podemos decir qué campo(s) deberían estar en nuestro formulario.

from django import forms

from .models import Post 


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","text")




1. CREAMOS ENLACE A UNA PAGINA PARA CONECTAR CON EL FORMULARIO

    Ahora toca abrir el fichero blog/templates/blog/base.html en el editor.

<a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>

    Ten en cuenta que queremos llamar a nuestra nueva vista post_new. La clase "glyphicon glyphicon-plus" es proporcionada por el tema de bootstrap que estamos utilizando, y nos mostrará un signo de suma.


2. VISTA Post_new

    en blog/views.py agregar 
    - Desde fichero forms.py que hemos creado importados la funcion PostForm
    - from .forms import PostForm 


    - Creamos la funcion de la vista para Post_new 

3. CREAMOS LA PLANTILLA QUE HEMOS LLAMADO LA FUNCIO : PostForm()

    Tenemos que crear un fichero post_edit.html el el directorio blog/templates/blog

    Para hacer que un formulario funcione necesitamos varias cosas:

    - Tenemos que mostrar el formulario. Podemos hacerlo, por ejemplo, con un sencillo {{ form.as_p }}.
    - La línea anterior tiene que estar dentro de una etiqueta de formuLario HTML: <form method="POST">...</form>.
    - Necesitamos un botón Guardar. Lo hacemos con un botón HTML:
        - - <button type='submit'>Save</button>.
    - Finalmente justo después de abrir la etiqueta <form ...> tenemos que añadir 
        - - {% csrf_token %} {{form.as_p}}. 
        - ¡Esto es muy importante ya que hace que tus formularios sean seguros! Si olvidas este pedazo, Django se molestará cuando intentes guardar el formulario:


- GUARDAR FORMULARIO

    Para hacer que un formulario pueda mandar informacion tenemos que hacer.
    Cuando enviamos el formulario somos redirigidos a la misma vista, pero esta vez tenemos algunos datos adicionales en request, más específicamente en request.POST (el nombre no tiene nada que ver con un post del blog, se refiere a que estamos "publicando" -en inglés, posting- datos). ¿Recuerdas que en el archivo HTML la definición de <form> tenía la variable method="POST"? Todos los campos del formulario estan ahora en request.POST. No deberías renombrar la variable POST (el único nombre que también es válido para la variable method es GET, pero no tenemos tiempo para explicar cuál es la diferencia).

    En nuestra vista tenemos dos situaciones distintas que manejar: primero, cuando accedemos a la página por primera vez y queremos un formulario vacío, y segundo, cuando regresamos a la vista con los datos del formulario que acabamos de ingresar. Así que tenemos que añadir una condición (utilizaremos if para eso):

    En blog/views.py

    if request.method == "POST":
        form = PostForm(request.POST)
        [...]
    else:
        form = PostForm()


    -- REVISAR BIENE ESTA PARTE
def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        # verificar si todos los campos estan bien. Comprobamos que el formulario es valido
        if form.is_valid():
            post = form.save(commit =False)
            post.autor = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect ('post_detail' , pk=post.pk)
    else:
        form = PostForm()

    return render (request, 'blog/post_edit.html', {'form': form })





- VALIDACION DE FORMULARIOS 

    Un post del blog debe tener los campos title y text. En nuestro modelo Post no dijimos (a diferencia de published_date) que estos campos no son requeridos, así que Django, por defecto, espera que estén definidos.

    - No podemos subir informacion al blog sin tener completar los camposo requeridos.

    Django se encarga de validad los datos si estan puesto o no antes de subirlos. 


- EDITAR FORMULARIO

    Ahora sabemos cómo agregar un nuevo formulario. Pero, ¿qué pasa si queremos editar uno existente? 

    1. Abre blog/templates/blog/post_detail.html en el editor de código y añade la línea despues del {% endif %}

<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>

    2. Abre blog/urls.py en el editor y añade esta línea:

path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    3. Vamos a reusar la plantilla blog/templates/blog/post_edit.html, así que lo último que nos falta es una view.
        - Abre blog/views.py en el editor de código y añade esto al final del todo:

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
    [...]





- SEGURIDAD & AUTENTIFICARCION PARA PUBLICAR

    ¡Poder crear nuevas publicaciones haciendo click en un enlace es genial! Pero, ahora mismo, cualquiera que visite tu página podría publicar un nuevo post y seguro que eso no es lo que quieres. Vamos a hacer que el botón sea visible para ti pero no para nadie más.

    Abre blog/templates/blog/base.html en el editor, busca el div page-header y la etiqueta del enlace (anchor) que pusimos antes. Debería ser algo así:

    blog/templates/blog/base.html
<a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>

    Vamos a añadir otra etiqueta {% if %} que hará que el enlace sólo parezca para los usuarios que hayan iniciado sesión en el admin.




    Tenemos que agregar una condicion que solo permita que los usuarios que han iniciado sesion puedan publicar 

{% if user.is_authenticated %}

<a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>

{% if user.is_authenticated %}



    Tambien tenemos que agregar eso en button que esta en blog/templates/blog/post_detail.html. 

{%if user.is_authenticated %}

<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>

{% endif %}



- PRUEBA DE AUTENTIFICACION 

Dado que es probable que estés conectado, si actualizas la página, no verás nada diferente. Carga la página en un navegador diferente o en una ventana en modo incógnito ("privado" en Windows Edge) y verás que el link no aparece, y el icono tampoco!














## ------------ MANEJO DE ERRORES  ---------------

1. NoReverseMatch at / : AUN NO HEMOS PASADO LA URL AL PATH 
    - path('post/new', views.post_new, name='post_new'),
        - En este caso al path de blog/urls.py

2. AttributeError: module 'blog.views' has no attribute 'post_new'
    - no hemos creado en blog/views la funcion para vista de post_new



