from django.urls import path
from . import views

urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    # Other URL patterns go here
    path('add/', views.add_thread, name='add_thread'),
    path('add/addPost/', views.add_thread_post, name='add_thread_post'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signup/kontuaSortu/', views.kontua_sortu, name='kontuaSortu'),
    path('login/auth/', views.auth, name='auth')
]
