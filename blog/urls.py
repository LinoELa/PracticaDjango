#Hemos creado este fichero es nuevo 


from django.urls import path

# from .views import 'FUNCION DE VIEWS.PY'  #ES LO MAS NORMAL HACER 
from . import views

#creamos nuestro propio patros URL para anadir la pagina 

urlpatterns = [
    path('', views.post_list , name='post_list')
]


