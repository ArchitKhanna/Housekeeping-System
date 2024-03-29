from django.urls import path
from .views import (
    AnnouncementListView,
    AnnouncementDetailView,
    AnnouncementCreateView,
    AnnouncementUpdateView,
    AnnouncementDeleteView,
    ApartmentListView,
    ApartmentDetailView,
    ApartmentCreateView,
    ApartmentUpdateView,
    ApartmentDeleteView
    )
from . import views


#On adding a new url, ensure views.name is correct, url is correct and name is changed.

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='hk-Home'),
    path('announcement/<int:pk>/', AnnouncementDetailView.as_view(), name='hk-announcement'),
    path('announcement/new/', AnnouncementCreateView.as_view(), name='hk-announcement-create'),
    path('announcement/<int:pk>/update/', AnnouncementUpdateView.as_view(), name='hk-announcement-update'),
    path('announcement/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='hk-announcement-delete'),
    path('tutorial/', views.tutorial, name='hk-Tutorial'),
    path('about/', views.about, name='hk-About'),
    path('gdpr-policy/', views.gdpr, name='hk-GDPR'),
    path('villagepanel/', ApartmentListView.as_view(), name='hk-villagepanel'),
    path('apartment/new/', ApartmentCreateView.as_view(), name='hk-apt-create'),
    path('apartment/<int:pk>/', ApartmentDetailView.as_view(), name='hk-Apartment'),
    path('apartment/<int:pk>/update/', ApartmentUpdateView.as_view(), name='hk-apt-update'),
    path('apartment/<int:pk>/delete/', ApartmentDeleteView.as_view(), name='hk-apt-delete'),
    path('completed/<int:pk>/<int:list_id>/<int:key>/', views.complete, name="task-complete"),
    path('undocomplete/<int:pk>/<int:list_id>/<int:key>', views.undocomplete, name="task-undo"),
    path('setcallback/<int:pk>/<int:list_id>/<int:key>/', views.setcallback, name="callback-set"),
    path('undocallback/<int:pk>/<int:list_id>/<int:key>', views.undocallback, name="callback-undo"),
]

handler400 = 'HKmanager.views.custom400'
handler403 = 'HKmanager.views.custom403'
handler404 = 'HKmanager.views.custom404'
handler500 = 'HKmanager.views.custom500'
