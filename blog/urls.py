#Hemos creado este fichero es nuevo 


from django.urls import path

# from .views import 'FUNCION DE VIEWS.PY'  #ES LO MAS NORMAL HACER 
from . import views

#creamos nuestro propio patros URL para anadir la pagina 

urlpatterns = [
    path('', views.post_list , name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]




