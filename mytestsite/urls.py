"""
URL configuration for mytestsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView

from django.contrib import admin
from django.urls import path, re_path
from polls import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# C:\Users\user\django_test\mytestsite

#workon my_django_environment

#py manage.py runserver

urlpatterns = [
    path('', views.api_root),

    path('admin/', admin.site.urls),
    
    re_path(r'^api/actors/$', views.actor_list, name='actor-list'),
    path('api/actor/<int:actor_id>/', views.ActorDetailView.as_view(), name='actor-detail'),    
    re_path(r'^api/actor_update/(\d+)$', views.actor_update, name='actor-update'),
    
    re_path(r'^api/genres/$', views.genre_list, name='genre-list'),
    re_path(r'^api/genre/(\d+)/$', views.genre_detail),
    re_path(r'^api/genre_update/(\d+)$', views.genre_update),
    

    
    # re_path(r'^api/movies/$', views.movie_list),
    re_path(r'^api/movie/(\d+)$', views.MovieDeleteView.as_view(), name='movie-detail'),
    re_path(r'^api/movie_update/(\d+)$', views.movie_update),
    re_path(r'^api/movies/$', views.MovieListView.as_view(), name='movie-list'),
    
    # path('', RedirectView.as_view(url='/api/movies/', permanent=True)),

]

