from django.conf import settings
from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from .serializers import CalendarItemSerializer
from phookit.bookingcalendar.models import CalendarItem


# TODO: Move into permissions.py
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        ### return obj.owner == request.user
        return obj.is_editable(request)

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to admins
        return request.user.is_staff


class CalendarItemList(generics.ListCreateAPIView):
    '''
    Only admins can create new calendar items
    '''
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly,)
    serializer_class = CalendarItemSerializer


    def get_queryset(self):
        """
        """
        queryset = CalendarItem.objects.all()
        start = self.request.QUERY_PARAMS.get('start', None)
        end = self.request.QUERY_PARAMS.get('end', None)
        if start and end:
            #queryset = queryset.filter(calendaritem__start_day>=start).filter(calendaritem__end_day<=end)
            #queryset = queryset.filter(start__gte=start).filter(end__lte=end)
            queryset = queryset.filter(Q(start__gte=start) | Q(end__lte=end))
        return queryset


class CalendarItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CalendarItem.objects.all()
    serializer_class = CalendarItemSerializer
