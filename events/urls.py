from . import views
from django.urls import path
from .views import OldEventList, DeleteSignUp


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('old-events/', OldEventList.as_view(), name='old_events'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
    path('like/<slug:slug>', views.EventLike.as_view(), name='event_like'),
    path('event/<slug:slug>/delete_signup/<int:signup_id>/', DeleteSignUp.as_view(), name='delete_signup'),   
]
