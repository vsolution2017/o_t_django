from django.conf.urls import url
from . import views
app_name = "panel"

urlpatterns = [
    url(r'^home/', views.home),
    url(r'^admin/', views.admin),
    url(r'^contratistas/load/$', views.load_contratistas, name = 'contratista_load'),
    url(r'^maquinarias/load$', views.load_maquinaria, name = 'maquinaria_load'),
    url(r'^mantenimiento/load/$', views.load_mantenimiento, name = 'mantenimiento_load'),
    url(r'^parroquia/load/$', views.load_parroquia, name = 'parroquia_load'),
    url(r'^actividad/load/$', views.load_actividad, name = 'actividad_load'),
]