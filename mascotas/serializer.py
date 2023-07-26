from rest_framework import serializers
from .models import Mascota,Developer,Juguete,Juguete_Mascota

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

class JugueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juguete
        fields = '__all__'

class JugueteMascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juguete_Mascota
        fields = '__all__'