from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Equipo, Mantenimiento, Lectura
from .serializers import EquipoSerializer, MantenimientoSerializer, LecturaSerializer

@api_view(['GET'])
def get_equipos(request):
    equipos = Equipo.objects.all()
    serializer = EquipoSerializer(equipos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_mantenimientos(request):
    mantenimientos = Mantenimiento.objects.all()
    serializer = MantenimientoSerializer(mantenimientos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_lecturas(request):
    lecturas = Lectura.objects.all()
    serializer = LecturaSerializer(lecturas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_equipo(request):
    serializer = EquipoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_mantenimiento(request):
    serializer = MantenimientoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_lectura(request):
    serializer = LecturaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
