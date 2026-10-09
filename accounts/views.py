from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User

def register(request):
  data = ''
  errors = []

  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    data = request.POST

    if password1 != password2:
      errors.append('La contraseña no coincide.')

    if User.objects.filter(username=username).exists():
      errors.append('El nombre de usuario ya existe.')

    if not errors:
      user = User.objects.create_user(
        username=username, 
        email=email, 
        first_name=first_name, 
        last_name=last_name, 
        password=password1,
      )
      login(request, user)
      return redirect('home') 
  
  return render(request, 'register.html', {'data': data, 'errors': errors})