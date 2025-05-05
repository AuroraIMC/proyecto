from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    #inicio 
    path('', views.inicio, name='inicio'),
    #registro usuario
    path('registro/', views.registro, name='registro'),
    #login y log out
    path('login/', auth_views.LoginView.as_view(template_name='catalogo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #perfil editar y cambiar contraseña
    path('accounts/profile/', views.perfil_usuario, name='perfil'),
    path('accounts/profile/editar/', views.editar_perfil, name='editar_perfil'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='catalogo/cambiar_contraseña.html',
        success_url='/accounts/password_change/done/'
    ), name='cambiar_contraseña'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='catalogo/cambiar_contraseña_done.html'
    ), name='cambiar_contraseña_hecho'),
    #libro nuevo 
    path('libros/nuevo/', views.registrar_libro, name='registrar_libro'),
    path('libros/<int:libro_id>/editar/', views.editar_libro, name='editar_libro'),
    path('libros/<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),

]
