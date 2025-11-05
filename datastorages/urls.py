from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_dashboard, name='data_dashboard'),
    path('generate/', views.generate_data, name='generate_data'),
    path('import/', views.import_data, name='import_data'),
    path('clear/', views.clear_data, name='clear_data'),
    path('export/', views.export_data, name='export_data'),
]