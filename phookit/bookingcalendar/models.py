from django.db import models

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

class CalendarItem(models.Model):
    start = models.DateField()
    end = models.DateField()
    title = models.CharField(max_length=128)
    url = models.URLField(null = True, blank = True)
    status = models.CharField(choices=BOOKING_STATUS_CHOICES, default=BOOKING_STATUS_CHOICES[0][0], max_length=20)
