from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop_home, name='shop_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.ShopDetailView.as_view(), name='shop_detail'),
    path('<int:pk>/update', views.ShopUpdateView.as_view(), name='shop_update'),
    path('<int:pk>/delete', views.ShopDeleteView.as_view(), name='shop_delete'),
]
