
from django.conf import settings
from rest_framework import serializers
from rest_framework import pagination
from rest_framework.reverse import reverse

from ..models import CalendarItem


class CalendarItemSerializer(serializers.ModelSerializer):

    backgroundColor = serializers.SerializerMethodField()

    class Meta:
        model = CalendarItem
        fields = ('id', 'start', 'end', 'title', 'url', 'status', 'backgroundColor', )


    def get_backgroundColor(self, obj):
        result = 'white'
        if obj.status == 'Booked':
            result = 'red'
        if obj.status == 'Reserved':
            result = 'blue'
        return result
