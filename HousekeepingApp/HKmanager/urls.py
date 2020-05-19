from django.urls import path
from . import views

#On adding a new url, ensure views.name is correct, url is correct and name is changed.

urlpatterns = [
    path('home/', views.home, name='hk-Home'),
    path('tutorial/', views.tutorial, name='hk-Tutorial'),
    path('thomondvillage/', views.thomondvillage, name='hk-ThomondVillage'),
]
