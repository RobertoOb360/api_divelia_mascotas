from django.contrib import admin
from .models import Developer,Juguete,Juguete_Mascota,Mascota
# Register your models here.

admin.site.register(Developer)
admin.site.register(Juguete)
admin.site.register(Juguete_Mascota)
admin.site.register(Mascota)