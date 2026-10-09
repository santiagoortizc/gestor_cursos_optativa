from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test

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

def is_admin(user):
  return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def groups(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    print("creando",name)
    if name and not Group.objects.filter(name=name).exists():
      Group.objects.create(name=name)
    return redirect('groups')

  groups = Group.objects.all()
  return render(request, 'groups.html', {'groups': groups})

@user_passes_test(is_admin)
def delete_group(request, group_id):
  if request.method == 'POST':
    group = get_object_or_404(Group, id=group_id)
    if group:
      group.delete()

  return redirect('groups')

def give_members(group):
  return group.user_set.all()

def give_non_members(group):
  members = group.user_set.all()
  return User.objects.exclude(id__in=members.values_list('id', flat=True))

@user_passes_test(is_admin)
def edit_group(request, group_id):
  group = get_object_or_404(Group, id=group_id)
  if request.method == 'POST':
    new_name = request.POST.get('name')
    group.name = new_name
    group.save()
    return redirect('groups')

  members = give_members(group)
  non_members = give_non_members(group)
  return render(request, 'edit_group.html', {'group': group, 'members': members, 'non_members': non_members})

@user_passes_test(is_admin)
def add_user_group(request, group_id):
  group = get_object_or_404(Group, id=group_id)
  if request.method == 'POST':
    user_id = request.POST.get('user_id')
    if user_id:
      user = get_object_or_404(User, id=user_id)
      group.user_set.add(user)

  return redirect('edit_group', group_id=group.id)

@user_passes_test(is_admin)
def remove_user_group(request, group_id):
  group = get_object_or_404(Group, id=group_id)
  if request.method == 'POST':
    user_id = request.POST.get('user_id')
    if user_id:
      user = get_object_or_404(User, id=user_id)
      group.user_set.remove(user)

  return redirect('edit_group', group_id=group.id)