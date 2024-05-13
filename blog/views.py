from django.shortcuts import render , get_object_or_404

from django.utils import timezone
from .models import Post

from .forms import PostForm

#   ir inmediatamente a la página post_detail del nuevo post, 
from django.shortcuts import redirect


# Create your views here.


#Creamos nuestra primera vista 

# REQUEST : Todo lo que recibimos del usuario via internet 

def post_list (request):

    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')

    return render (request, 'blog/post_list.html', {'posts':posts})



# NUEVA VISTA 
def post_detail (request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render (request , 'blog/post_detail.html' , {'post':post})


# NUEVA VISTA : Para  formulacion

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


#  VAMOS A REUTILIZARLO : Editar formulario


def post_edit(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
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
