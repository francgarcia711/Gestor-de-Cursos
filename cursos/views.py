from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import CursoFormulario, ProfesorFormulario, ProfesorForm

def inicio(request):
    return render(request, 'Cursos/inicio.html')

def lista_estudiantes(request):
    Estudiantes = Estudiante.objects.all()
    return render(request, 'Cursos/estudiantes_list.html', {'estudiantes': Estudiantes})

def detalle_estudiante(request, pk):
    Estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'Cursos/estudiante_detail.html', {'estudiante': Estudiante})

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'Cursos/profesores_list.html', {'profesores': profesores})

def lista_entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'Cursos/entregables_list.html', {'entregables': entregables})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'Cursos/cursos.html', {'cursos': cursos})

def cursoFormulario(request):
    if request.method == 'POST':
        form = CursoFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            camada = form.cleaned_data['camada']
            curso = Curso(nombre=nombre, camada=camada)
            curso.save()
            return render(request, 'Cursos/curso_exito.html')
    else:
        form = CursoFormulario()
    return render(request, 'Cursos/curso_formulario.html', {'form': form})

def profesorFormulario(request):
    if request.method == 'POST':
        form = ProfesorFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            profesion = form.cleaned_data['profesion']
            profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profesor.save()
            return redirect('cursos:lista_profesores') # Redirige a la lista de profesores
    else:
        form = ProfesorFormulario()
    return render(request, 'Cursos/profesor_formulario.html', {'form': form})

def profesor_editar(request, id):
    profesor = get_object_or_404(Profesor, id=id)

    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('cursos:lista_profesores')
    else:
        form = ProfesorForm(instance=profesor)

    return render(request, 'Cursos/profesor_editar.html', {'form': form, 'profesor': profesor})

def profesor_eliminar(request, id):
    profesor = get_object_or_404(Profesor, id=id)

    if request.method == 'POST':
        profesor.delete()
        return redirect('cursos:lista_profesores')

    return render(request, 'Cursos/profesor_confirm_delete.html', {'profesor': profesor})

def buscar(request):

    if request.GET.get("camada"):
        camada = request.GET.get("camada")
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "Cursos/resultados_busqueda.html", {"cursos": cursos, "camada": camada})
    else:
        return render(request, "Cursos/resultados_busqueda.html", {"cursos": []})
    
def buscar_profesor(request):
    if request.GET.get("query"):
        query = request.GET.get("query")
        # Buscamos coincidencias en el campo 'apellido'
        profesores = Profesor.objects.filter(apellido__icontains=query)

        return render(request, "Cursos/resultados_busqueda_profesores.html", {"profesores": profesores, "query": query})
    else:
        return render(request, "Cursos/resultados_busqueda_profesores.html", {"profesores": []})