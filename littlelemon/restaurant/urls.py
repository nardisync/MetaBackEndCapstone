
from django.contrib import admin
from django.urls import path, include
from .views import sayHello, index, MenuItemsView, SingleMenuItemView, BookingViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'tables', BookingViewSet)


urlpatterns = [
    #path('', sayHello, name='sayHello'),
    path('', include(router.urls)),
    #path('', index, name='index'),
    path('api-token-auth/', obtain_auth_token),
    # ---------------------------------------------------------
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    # ---------------------------------------------------------
    path('booking/', include(router.urls)),
]
