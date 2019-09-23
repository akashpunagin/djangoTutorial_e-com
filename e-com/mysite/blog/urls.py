from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogName'),
    # path('blogpost/', views.blogpost, name='blogPage'),
    path('blogpost/<int:id>',views.blogpost,name='productview'),


]
