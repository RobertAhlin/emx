from . import views
from django.urls import path
from .views import OldEventList, DeleteSignUp, EditSignUp


urlpatterns = [
    # Home page displaying the list of upcoming events
    path('', views.EventList.as_view(), name='home'),

    # Page displaying the list of past events
    path('old-events/', OldEventList.as_view(), name='old_events'),

    # Detail page for a specific event identified by its slug
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),

    # Like/unlike an event
    path('like/<slug:slug>', views.EventLike.as_view(), name='event_like'),

    # Edit a sign-up for event
    path('event/<slug:slug>/edit_signup/<int:signup_id>/',
         EditSignUp.as_view(), name='edit_signup'),

    # Delete a sign-up from event
    path('event/<slug:slug>/delete_signup/<int:signup_id>/',
         DeleteSignUp.as_view(), name='delete_signup'),
]
