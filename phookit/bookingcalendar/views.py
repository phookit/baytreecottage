from django.shortcuts import render
from django.db.models import Q
import datetime

from phookit.core.paginator import paginate
from .models import BookingPrice


def index(request):
    # get all prices from todays range and paginate
    today = datetime.datetime.today()
    queryset = BookingPrice.objects.filter(Q(start__gte=today) | Q(end__gte=today))
    prices = paginate(queryset, request)
    return render(request, 'bookingcalendar/index.html', {'prices': prices})
