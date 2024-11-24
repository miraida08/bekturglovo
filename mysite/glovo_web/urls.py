from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', ProductViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),


    path('profile/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('profile/<int:pk>/', UserViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='user_detail'),


    path('store/', StoreViewSet.as_view({'get': 'list', 'post': 'create'}), name='store_list'),
    path('store/<int:pk>/', StoreViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='store_detail'),


    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='category_detail'),



    path('order/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order_list'),
    path('order/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='order_detail'),


    path('courier/', CourierViewSet.as_view({'get': 'list', 'post': 'create'}), name='courier_list'),
    path('courier/<int:pk>/', CourierViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='courier_detail'),


    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='review_detail'),
]