from django.urls import path 
from . import views

urlpatterns = [
    path('getStud/', views.getStud),
    path('postStud/', views.postStud),
    path('putStud/', views.putStud),
    path('patchStud/', views.patchStud),
]
