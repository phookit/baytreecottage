from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 


"""
Available : Time is available to book
Reserved : Time has been ordered but not fully booked (Not paid for)
Booked : Time has been booked and paid for.
"""
BOOKING_STATUS_CHOICES = (
    ('Available', 'Available'),
    ('Reserved',  'Reserved'),
    ('Booked',    'Booked'),
)

class Booking(models.Model):
    start = models.DateField()
    end = models.DateField()
    name = models.CharField(max_length=1024)
    email = models.EmailField(null = True, blank = True)
    tel = models.CharField(max_length=32)

    info = models.TextField(max_length=1024, null = True, blank = True)
    status = models.CharField(choices=BOOKING_STATUS_CHOICES, default=BOOKING_STATUS_CHOICES[1][0], max_length=20)

    class Meta:
        ordering = ("start",)

    def __str__(self):
        return "%s : %s : %s->%s" % (self.name, self.status, self.start, self.end)

 
class BookingPrice(models.Model):
    start = models.DateField()
    end = models.DateField()
    price = models.CharField(max_length=10)

    class Meta:
        ordering = ("start",)

    def __str__(self):
        return "%s -> %s : %s" % (self.start, self.end, self.price)
