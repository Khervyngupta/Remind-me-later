from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):

    reminder_type = serializers.ChoiceField(choices=['SMS', 'Email'])
    class Meta:
        model = Reminder
        fields = ['date', 'time', 'message', 'reminder_type']
