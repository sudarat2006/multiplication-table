from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('for/', views.for_view, name='for'),
    path('multipli/', views.multipli, name='multipli'),
]