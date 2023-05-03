
from django.contrib import admin
from django.urls import path, include
#from .restaurant.views import BookingViewSet



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/menu/',include('restaurant.urls')),
    
]