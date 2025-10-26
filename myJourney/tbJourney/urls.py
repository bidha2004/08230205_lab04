from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),         # Root URL -> index.html
    path('about.html', views.aboutMe, name='about'), # /about -> aboutMe.html
]
