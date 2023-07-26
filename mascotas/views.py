from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import DeveloperSerializer, MascotaSerializer, JugueteSerializer, JugueteMascotaSerializer
from .models import Developer, Mascota, Juguete, Juguete_Mascota

class DeveloperListCreateView(generics.ListCreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class DeveloperRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class MascotaListCreateView(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class MascotaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class JugueteListCreateView(generics.ListCreateAPIView):
    queryset = Juguete.objects.all()
    serializer_class = JugueteSerializer

class JugueteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Juguete.objects.all()
    serializer_class = JugueteSerializer

class AsociarJugueteMascotaView(generics.CreateAPIView):
    serializer_class = JugueteMascotaSerializer

    def create(self, request, *args, **kwargs):
        # Obtener la mascota
        mascota_id = kwargs.get('mascota_id')
        try:
            mascota = Mascota.objects.get(id=mascota_id)
        except Mascota.DoesNotExist:
            return Response({"detail": "Mascota no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
        if Juguete_Mascota.objects.filter(mascota=mascota).count() >= 3:
            return Response({"detail": "La mascota ya tiene el máximo de juguetes permitidos."}, status=status.HTTP_400_BAD_REQUEST)

        # Asociar el juguete a la mascota y guardar
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(mascota=mascota)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
