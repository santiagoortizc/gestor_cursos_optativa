from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('register/', views.register, name='register'),
  path('groups/', views.groups, name='groups'),
  path('groups/<int:group_id>/edit', views.edit_group, name='edit_group'),
  path('groups/<int:group_id>/add-user', views.add_user_group, name='add_user_group'),
  path('groups/<int:group_id>/remove-user', views.remove_user_group, name='remove_user_group'),
  path('groups/<int:group_id>/delete', views.delete_group, name='delete_group'),
  path('permissions/', views.permissions, name='permissions'),

]