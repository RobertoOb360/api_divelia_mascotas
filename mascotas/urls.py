from django.urls import path
from .views import (
    DeveloperListCreateView,
    DeveloperRetrieveUpdateDestroyView,
    MascotaListCreateView,
    MascotaRetrieveUpdateDestroyView,
    JugueteListCreateView,
    JugueteRetrieveUpdateDestroyView,
    AsociarJugueteMascotaView,
)

urlpatterns = [
    path('developers/', DeveloperListCreateView.as_view(), name='developer-list-create'),
    path('developers/<int:pk>/', DeveloperRetrieveUpdateDestroyView.as_view(), name='developer-detail'),
    path('mascotas/', MascotaListCreateView.as_view(), name='mascota-list-create'),
    path('mascotas/<int:pk>/', MascotaRetrieveUpdateDestroyView.as_view(), name='mascota-detail'),
    path('juguetes/', JugueteListCreateView.as_view(), name='juguete-list-create'),
    path('juguetes/<int:pk>/', JugueteRetrieveUpdateDestroyView.as_view(), name='juguete-detail'),
    path('mascotas/<int:mascota_id>/asociar-juguete/', AsociarJugueteMascotaView.as_view(), name='asociar-juguete-mascota'),
]