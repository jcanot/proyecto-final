from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import formAutor, formArticulo, formSeccion
from blog.models import *

# Create your views here.


def menu(request):

    return render(request, "blog/padre.html")


def articulo(request):

    articulos = Articulo.objects.all()
    contexto = {"articulos": articulos}
    return render(request, "blog/articulo.html", contexto)


def autor(request):

    autores = Autor.objects.all()
    contexto = {"autores": autores}

    return render(request, "blog/autor.html", contexto)


def seccion(request):

    secciones = Seccion.objects.all()
    contexto = {"secciones": secciones}
    return render(request, "blog/seccion.html", contexto)


def cargarArticulo(request):
    if request.method == "POST":

        miFormulario = formArticulo(request.POST)  # aqui me llega la info del html
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            articulo = Articulo(
                titulo=informacion["titulo"], texto=informacion["texto"]
            )

            articulo.save()

            return render(request, "blog/padre.html")

    else:

        miFormulario = formArticulo()

    return render(request, "blog/cargarArticulo.html", {"miFormulario": miFormulario})


def cargarAutor(request):
    if request.method == "POST":

        miFormulario = formAutor(request.POST)  # aqui me llega la info del html
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            autor = Autor(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                profesion=informacion["profesion"],
            )

            autor.save()

            return render(request, "blog/padre.html")

    else:

        miFormulario = formAutor()

    return render(request, "blog/cargarAutor.html", {"miFormulario": miFormulario})


def cargarSeccion(request):
    if request.method == "POST":

        miFormulario = formSeccion(request.POST)  # aqui me llega la info del html
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            seccion = Seccion(nombre=informacion["nombre"])

            seccion.save()

            return render(request, "blog/padre.html")

    else:

        miFormulario = formSeccion()

    return render(request, "blog/cargarSeccion.html", {"miFormulario": miFormulario})


def busqueda(request):
    return render(request, "blog/busqueda.html")


def buscar(request):

    if request.GET["autor"]:

        nombre = request.GET["autor"]
        autores = Autor.objects.filter(nombre__icontains=nombre)
        contexto = {"autores": autores, "nombre": nombre}

        return render(request, "blog/resultadoBusquedaAutor.html", contexto)

    else:
        respuesta = "no enviaste datos"
        return HttpResponse(respuesta)
