from django.urls import path
from .import views

app_name = 'fileIO'

urlpatterns = [
    path('excel/', views.response_excel),
    path('excel2/', views.response_excel2),
    path('image/', views.response_pillow_image)
]
