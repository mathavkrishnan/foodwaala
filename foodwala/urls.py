from django.contrib import admin
from django.urls import path
from products import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',views.prod_list,name='list'),
    path('create/',views.prod_create,name='create'),
    path('create_cart/',views.cart_create,name='create_cart'),
    path('<int:pk>/',views.prod,name='specific'),
    path('auth/',obtain_auth_token),
    path('user_register/',views.user_register,name='user_register'),
    path('listcart/',views.cart_list,name='listcart'),
    path('delete_cart/',views.delete_cart,name='delete_cart'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
