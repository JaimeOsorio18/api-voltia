from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Equipo, Mantenimiento, Lectura
from .serializers import EquipoSerializer, MantenimientoSerializer, LecturaSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['GET'])
def main_view(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response('Token is missing', status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = JWTAuthentication().authenticate(request)
        if user is None:
            return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    except InvalidToken:
        return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    equipos = Equipo.objects.all()
    mantenimientos = Mantenimiento.objects.all()
    lecturas = Lectura.objects.all()

    equipo_serializer = EquipoSerializer(equipos, many=True)
    mantenimiento_serializer = MantenimientoSerializer(mantenimientos, many=True)
    lectura_serializer = LecturaSerializer(lecturas, many=True)

    data = {
        'equipos': equipo_serializer.data,
        'mantenimientos': mantenimiento_serializer.data,
        'lecturas': lectura_serializer.data
    }

    return Response(data)

@api_view(['GET'])
def get_equipos(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response('Token is missing', status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = JWTAuthentication().authenticate(request)
        if user is None:
            return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    except InvalidToken:
        return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    equipos = Equipo.objects.all()
    serializer = EquipoSerializer(equipos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_mantenimientos(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response('Token is missing', status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = JWTAuthentication().authenticate(request)
        if user is None:
            return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    except InvalidToken:
        return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    mantenimientos = Mantenimiento.objects.all()
    serializer = MantenimientoSerializer(mantenimientos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_lecturas(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response('Token is missing', status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = JWTAuthentication().authenticate(request)
        if user is None:
            return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    except InvalidToken:
        return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    lecturas = Lectura.objects.all()
    serializer = LecturaSerializer(lecturas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_equipo(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response('Token is missing', status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = JWTAuthentication().authenticate(request)
        if user is None:
            return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    except InvalidToken:
        return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    serializer = EquipoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_mantenimiento(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response('Token is missing', status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = JWTAuthentication().authenticate(request)
        if user is None:
            return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    except InvalidToken:
        return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    serializer = MantenimientoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_lectura(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response('Token is missing', status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = JWTAuthentication().authenticate(request)
        if user is None:
            return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    except InvalidToken:
        return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    serializer = LecturaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def cargar_ejemplos(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response('Token is missing', status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = JWTAuthentication().authenticate(request)
        if user is None:
            return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    except InvalidToken:
        return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    insertar_ejemplos_django()
    return Response("Ejemplos cargados correctamente.", status=200)

def insertar_ejemplos_django():
    equipo1 = Equipo(nombre='Generador', tipo='Generación', ubicacion='Sala de máquinas')
    equipo2 = Equipo(nombre='Transformador', tipo='Distribución', ubicacion='Subestación')
    equipo3 = Equipo(nombre='Motor', tipo='Consumo', ubicacion='Taller')
    equipo1.save()
    equipo2.save()
    equipo3.save()

    mantenimiento1 = Mantenimiento(equipo=equipo1, fecha='2022-01-15', descripcion='Cambio de aceite')
    mantenimiento2 = Mantenimiento(equipo=equipo2, fecha='2022-03-10', descripcion='Prueba de aislamiento')
    mantenimiento3 = Mantenimiento(equipo=equipo3, fecha='2022-05-20', descripcion='Reemplazo de rodamientos')
    mantenimiento1.save()
    mantenimiento2.save()
    mantenimiento3.save()

    lectura1 = Lectura(equipo=equipo1, fecha='2022-01-01', valor='1200 kW')
    lectura2 = Lectura(equipo=equipo1, fecha='2022-02-01', valor='1250 kW')
    lectura3 = Lectura(equipo=equipo2, fecha='2022-03-01', valor='500 kVA')
    lectura1.save()
    lectura2.save()
    lectura3.save()

@api_view(['GET'])
def protected_view(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response('Token is missing', status=status.HTTP_401_UNAUTHORIZED)

    try:
        user = JWTAuthentication().authenticate(request)
        if user is None:
            return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    except InvalidToken:
        return Response('Invalid token', status=status.HTTP_401_UNAUTHORIZED)
    return Response({'message': 'Esta es una ruta protegida. Solo se puede acceder con un token válido.'})

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Se requiere nombre de usuario y contraseña.'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'El nombre de usuario ya está registrado.'}, status=400)

    user = User(username=username, password=make_password(password))
    user.save()

    refresh = RefreshToken.for_user(user)

    return Response({
        'message': 'Usuario registrado exitosamente.'
    })

@api_view(['POST'])
def login(self, request):
    username = request.data.get('usuario')
    password = request.data.get('contraseña')

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token})
        
    return Response({'error': 'Credenciales inválidas'}, status=401)

