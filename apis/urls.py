from django.urls import path
from .views import ReminderCreateView, ReminderListView

urlpatterns = [
    path('reminders/create/', ReminderCreateView.as_view(), name='reminder-create'),
    path('reminders/list/', ReminderListView.as_view(), name='reminder-list'),
]
