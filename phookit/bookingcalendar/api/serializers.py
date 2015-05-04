
from django.conf import settings
from rest_framework import serializers
from rest_framework import pagination
from rest_framework.reverse import reverse

from ..models import Booking

class BookingSerializer(serializers.ModelSerializer):

    backgroundColor = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ('id', 'start', 'end', 'status', 'backgroundColor', )


    def get_backgroundColor(self, obj):
        result = '#beffaf'
        if obj.status == 'Booked':
            result = '#d29898'
        if obj.status == 'Reserved':
            result = '#b9beff'
        return result


class BookingAdminSerializer(BookingSerializer):

    class Meta:
        model = Booking
        fields = ('id', 'start', 'end', 'name', 'email', 'tel', 'info', 'status', 'backgroundColor', )
