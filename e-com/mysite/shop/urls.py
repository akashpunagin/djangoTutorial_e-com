from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopName'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('tracker/',views.tracker,name='tracker'),
    path('search/',views.search,name='search'),
    path('products/<int:myid>',views.productview,name='productview'),
    path('checkout/',views.checkout,name='checkout'),


]
