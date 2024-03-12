from django.shortcuts import render
from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer

# Create your views here.

class ReminderCreateView(generics.CreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

class ReminderListView(generics.ListAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer