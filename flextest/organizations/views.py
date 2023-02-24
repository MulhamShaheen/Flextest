from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .serializers import *

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.authentication import JWTAuthentication




class Autherization(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        data = JSONParser().parse(request)
        
        email = data['email']
        password = data['password']
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            
            refresh = RefreshToken.for_user(user)
            
            return Response({
                
                        'data': str(user),
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                             
                        }, status=200)
        # Redirect to a success page.
        
        else:
            # Return an 'invalid login' error message.
            return Response({"msg": "invalid login"}, status=400)


@api_view(['POST'])
def regester(request):
    data = JSONParser().parse(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        login(request, user)
        refresh = RefreshToken.for_user(user)
        
        return Response({
                    'data':serializer.data, 
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),}, status=201)
    else:
        return Response(serializer.errors, status=400)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    data = JSONParser().parse(request)
    user = request.user
    data["email"] = user.email
    data["password"] = user.password
    
    serializer = UserSerializer(user, data=data)
    if serializer.is_valid():
            serializer.update(user, data)
            return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
    
@api_view(['GET'])
def get_users(request, id=None):
    if id is None:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
    else:
        user = User.object.get(id=id) 
        serializer = UserSerializer(user)
   
    return Response(serializer.data)


@api_view(['POST'])
def create_organization(request):
    data = JSONParser().parse(request)
    serializer = OrganizationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_organizations(request):
    organizations = Organization.objects.all()
    serializer = OrganizationListSerializer(organizations, many=True)
    
    return Response(serializer.data)