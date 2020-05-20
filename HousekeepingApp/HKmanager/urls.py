from django.urls import path
from .views import (
    ApartmentListView,
    ApartmentDetailView,
    ApartmentCreateView,
    ApartmentUpdateView,
    ApartmentDeleteView
    )
from . import views


#On adding a new url, ensure views.name is correct, url is correct and name is changed.

urlpatterns = [
    path('home/', views.home, name='hk-Home'),
    path('tutorial/', views.tutorial, name='hk-Tutorial'),
    path('thomondvillage/', ApartmentListView.as_view(), name='hk-ThomondVillage'),
    path('apartment/new/', ApartmentCreateView.as_view(), name='hk-apt-create'),
    path('apartment/<int:pk>/', ApartmentDetailView.as_view(), name='hk-Apartment'),
    path('apartment/<int:pk>/update/', ApartmentUpdateView.as_view(), name='hk-apt-update'),
    path('apartment/<int:pk>/delete/', ApartmentDeleteView.as_view(), name='hk-apt-delete'),
]
