from django.urls import path
from .views import APIRoot, EventList, EventDetail, WorkshopList, WorkshopDetail

urlpatterns = [
    path('', APIRoot.as_view(), name="api-root"),
    path('events/', EventList.as_view(), name="event-list"),
    path('events/<int:pk>/', EventDetail.as_view(), name="event-detail"),
    path('workshops/', WorkshopList.as_view(), name="workshop-list"),
    path('workshops/<int:pk>/', WorkshopDetail.as_view(), name="workshop-detail"),
]