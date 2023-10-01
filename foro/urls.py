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
    path('login/auth/', views.auth, name='auth'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:thread_id>/', views.ezabatu, name='ezabatu'),
    path('autorea/<str:author>/', views.autorea, name='autorea'),
    path('haria/<int:thread_id>/', views.haria, name='haria'),
    path('haria/<int:thread_id>/addReply/', views.add_reply, name='add_reply'),
]
