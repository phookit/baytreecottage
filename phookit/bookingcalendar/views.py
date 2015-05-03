from django.shortcuts import render

from phookit.core.paginator import paginate
from .models import BookingPrice


# Create your views here.
def index(request):
    prices = paginate(BookingPrice.objects.all(), request)
    return render(request, 'bookingcalendar/index.html', {'prices': prices})
