from django.urls import path
from .views import ApartmentListView, ApartmentDetailView
from . import views


#On adding a new url, ensure views.name is correct, url is correct and name is changed.

urlpatterns = [
    path('home/', ApartmentListView.as_view(), name='hk-Home'),
    path('tutorial/', views.tutorial, name='hk-Tutorial'),
    path('thomondvillage/', ApartmentListView.as_view(), name='hk-ThomondVillage'),
]
