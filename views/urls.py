from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('home/',views.index, name="index"),
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name="home"),
    path('action/', views.action, name="action"),
    path('anime/', views.anime, name="anime"),
    path('comedy/', views.comedy, name="comedy"),
]