# Este es el archivo de  fromulario creado por  mi  para poder editar la base de datos desde aqui 
#Es una forma agradable de agregar y editar posts en el blog


from django import forms

from .models import Post 


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","text")



        


