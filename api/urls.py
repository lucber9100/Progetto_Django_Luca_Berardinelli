from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Ex.1
    path('new_post', views.new_post, name='new_post'), # Ex.2 + Ex.7
    path('admin_panel', views.admin_panel, name='admin_panel'),  # Ex.3
    path('utente/<int:pk>/', views.user_detail, name='user_detail'),  # Ex.4
    path('posts1h', views.posts1h, name='posts1h'), # Ex.5
    path('get_occurrences/<str:string>/', views.get_occurrences, name='get_occurrences'),  # Ex.6
    path('logged_in', views.logged_in, name='logged_in'),  # Ex.8
    # -------------------------------------------------------------------
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('accounts/login', include('django.contrib.auth.urls'), name='login'),
    path('accounts/logout', include('django.contrib.auth.urls'), name='logout')
]