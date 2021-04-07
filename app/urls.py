from django.urls import include, path
from . import views

urlpatterns = [
    path('api/get_categories/', views.CategoryViewSet.as_view({'get': 'list'})),
    path('api/get_category/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve'})),
    path('api/get_products/', views.ProductViewSet.as_view({'get': 'list'})),
    path('api/get_product/<int:pk>/', views.ProductViewSet.as_view({'get': 'retrieve'})),
    path('api/order/', views.OrderViewSet.as_view({'post': 'create'})),
]
