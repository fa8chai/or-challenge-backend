from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import User
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    email = request.data['email']
    password = request.data['password']
    user = authenticate(request, email=email, password=password)
    if user is not None and user.is_staff:
        login(request, user)
        return JsonResponse({
            'url': reverse('admin:login'),
            'user_found': True,
            'name': user.name,
            'email': user.email,
        })

    elif user is not None and not user.is_Staff:
        login(request, user)
        return JsonResponse({
            'user_found': True,
            'name': user.name,
            'email': user.email,
        })
    else:
        return JsonResponse({
            'user_found': False
        })

@api_view(['POST'])
@permission_classes([AllowAny])
def api_signup(request):
    email = request.data['email']
    password = request.data['password']
    name = request.data['name']
    user = User.objects.create(password = password, email = email, name = name )
    if user.save() :
        login(request, user)
        return JsonResponse({
            'success': True,
            'name': user.name,
            'email': user.email,
        })
    else:
        return JsonResponse({
            'success': False
        })