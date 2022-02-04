from django.shortcuts import render
from rest_framework.reverse import reverse

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Event, Workshop
from. serializers import EventSerializer, WorkshopSerializer

# Create your views here.
class APIRoot(APIView):
    def get(self, request):
        return Response({
            'Events': reverse('event-list', request=request),
            'Workshops': reverse('workshop-list', request=request)
        })
        
class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class WorkshopList(generics.ListAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    
class WorkshopDetail(generics.RetrieveAPIView):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer