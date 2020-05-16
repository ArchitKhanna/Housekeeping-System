from django.urls import path
from . import views

#On adding a new url, ensure views.name is correct, url is correct and name is changed. 

urlpatterns = [
    path('home/', views.home, name='HK-Home'),
    path('tutorial/', views.tutorial, name='HK-Tutorial'),
    path('thomondvillage/', views.thomondvillage, name='HK-ThomondVillage'),
]
