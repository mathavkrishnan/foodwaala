from django.shortcuts import render
from .models import Prod, Cart
#from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import ProdSerializers,UserSerializer, CartSerializers
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.



@api_view (['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def prod_list(request):
    product = Prod.objects.all()
    serializer = ProdSerializers(product,many=True)
    return Response(serializer.data)

@api_view (['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def prod_create(request):
    serializers = ProdSerializers(data=request.data)
    if serializers.is_valid():
        product = serializers.create(serializers.validated_data)
        product.save()
        return Response(serializers.data)
    else:
        return Response(serializers.errors)

@api_view (['GET','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def prod(request,pk):
    prod = Prod.objects.get(pk=pk)
    if request.method == 'GET':
      serializer = ProdSerializers(prod)
      return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PUT":
        serializer = ProdSerializers(prod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
def user_register(request):
    serializer = UserSerializer(data = request.data)
    if not serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    user = User.objects.get(username=serializer.data['username'])
    token_obj, _ = Token.objects.get_or_create(user=user)
    return Response({'payload': serializer.data, 'token': str(token_obj)}, status=200)
    


@api_view (['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cart_list(request):
    cart = Cart.objects.filter(username = request.user)
    ser = CartSerializers(cart,many=True)
    return Response(ser.data)

@api_view (['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cart_create(request):
    serializers = CartSerializers(data=request.data)
    if serializers.is_valid():
        cart = serializers.create(serializers.validated_data)
        cart.save()
        return Response(serializers.data)
    else:
        return Response(serializers.errors)

@api_view(['delete'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_cart(request):
     cart = Cart.objects.filter(username=request.user,title = request.data['title'])
     cart.delete()
     return Response(status=status.HTTP_204_NO_CONTENT)