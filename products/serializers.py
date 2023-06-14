from rest_framework import serializers
from .models import Prod
from django.forms import ValidationError
from django.contrib.auth.models import User
from .models import Cart

GEEKS_CHOICES =(
    ("1", "Breakfast"),
    ("2", "Lunch"),
    ("3", "Dinner"),
    ("4", "All"),
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],password = validated_data['password'])
        user.save()
        return user

class ProdSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    foodtype = serializers.ChoiceField(choices=GEEKS_CHOICES)
    rating = serializers.IntegerField()
    images = serializers.ImageField()

    def create(self,data):
        return Prod.objects.create(**data)
    
    def update(self,instance,data):
        instance.title = data.get('title',instance.title)
        instance.price = data.get('price',instance.price)
        instance.foodtype = data.get('foodtype',instance.foodtype)
        instance.rating = data.get('rating',instance.rating)
        instance.images = data.get('images',instance.images)
        instance.save()
        return instance

class CartSerializers(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Cart
        fields = ['username','title', 'price','images','quantity']

    def create(self,data):
        return Cart.objects.create(**data)