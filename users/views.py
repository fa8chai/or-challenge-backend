from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import User
from rest_framework.permissions import AllowAny
from django.core.exceptions import ValidationError


@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    email = request.data['email']
    password = request.data['password']
    user = authenticate(request, email=email, password=password)
    user = User.objects.get(email=email);
    if user and user.is_staff:
        login(request, user)
        return JsonResponse({
            'url': reverse('admin:login'),
            'user_found': True,
            'name': user.name,
            'email': user.email,
        })

    elif user and user.is_staff == False:
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
    try:
        user = User.objects.create(password = password, email = email, name = name )
        login(request, user)
        return JsonResponse({
            'success': True,
            'name': user.name,
            'email': user.email,
        })
    except ValidationError :         
        return JsonResponse({
            'success': False
        })
