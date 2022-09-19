from django.shortcuts import render
from .forms import CreateUsuarioForm, EditUsuarioForm
from .models import Usuario


# Create your views here.

def home_main(request):
    return render(request, 'main/home.html')

def create_users_main(request):
    data_result = {'form_create_user': CreateUsuarioForm()}
    if request.method == "POST":
       formulario = CreateUsuarioForm(request.POST)
       print(request.method)
       if formulario.is_valid():
            formulario.save()
            data_result['message'] = "Formulario valido"
    else:
            data_result['message'] = "Formulario no valido"
    print(data_result) 
    return render(request, 'main/createuser.html', data_result)

def list_users_main(request):
    usuarios = Usuario.objects.all()
    data_result = {'user_list':usuarios}
    return render(request, 'main/userslist.html', data_result)

def update_users_main(request, usuario_id):
    usuarios = Usuario.objects.get(pk= usuario_id)
    formulario = EditUsuarioForm()
    data_result = {'usuario': usuarios}
    data_result['formulario'] = formulario
    print(usuarios)

    if request.method =="POST":
        formulario =EditUsuarioForm(request.POST, instance= usuarios)
        print(request.POST)
        if formulario.is_valid():
            formulario.save()
            data_result['message'] = "usuario actualizado"
        else:
            data_result['message'] =  "usuario no actualizado"
    return render(request, 'main/updateuser.html',data_result)