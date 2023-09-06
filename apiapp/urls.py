# arduino_api/urls.py
from django.urls import path
from .views import UpdateSensorDataView

urlpatterns = [
    path('update-sensor-data/', UpdateSensorDataView.as_view(), name='update-sensor-data'),
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('update_data/', views.update_data, name='update_data'),
# ]