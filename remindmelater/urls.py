from django.contrib import admin
from django.urls import path
from reminder.views import ReminderAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/reminder/', ReminderAPIView.as_view()),
]
