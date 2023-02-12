from django.contrib import admin
from django.urls import path
from webapp import views


urlpatterns = [
    path('', views.index, name='home'),
    path('bba/', views.bba, name='bba'),
    path('bcom/', views.bcom, name='bcom'),
    path('ba/', views.ba, name='ba'),
    path('bsw/', views.bsw, name='bsw'),
    path('bsc/', views.bsc, name='bsc'),
    path('blis/', views.blis, name='blis'),
    path('mliss/', views.mlis, name='mlis'),
    path('mba/', views.mba, name='mba'),
    path('ma/', views.ma, name='ma'),
    path('JSS/', views.JSS, name='JSS'),
    path('Medical/', views.Medical, name='Medical'),
    path('BOSSE/', views.BOSSE, name='BOSSE'),
    path('register/', views.register, name='apply'),
]