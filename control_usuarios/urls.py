from django.urls import path
from .import views

urlpatterns = [
    path('', views.index_view, name="index_view"),
    path('preguntas/', views.preguntas_view, name="preguntas_view"),
    path('resultado/', views.resultado_view, name="resultado_view"),
]