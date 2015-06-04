from django.conf import settings
from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from .serializers import BookingSerializer, BookingAdminSerializer, BookingPriceAdminSerializer
from phookit.bookingcalendar.models import Booking, BookingPrice


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


class BookingList(generics.ListCreateAPIView):
    '''
    Only admins can create new calendar items
    '''
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly,)
    serializer_class = BookingSerializer


    def get_queryset(self):
        """
        """
        queryset = Booking.objects.all()
        start = self.request.QUERY_PARAMS.get('start', None)
        end = self.request.QUERY_PARAMS.get('end', None)
        if start and end:
            queryset = queryset.filter(Q(start__gte=start) | Q(end__lte=end))
        return queryset


class BookingAdminDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Booking.objects.all()
    serializer_class = BookingAdminSerializer


class BookingAdminList(generics.ListCreateAPIView):
    '''
    Only admins can create new calendar items
    '''
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = BookingAdminSerializer


    def get_queryset(self):
        """
        """
        queryset = Booking.objects.all()
        start = self.request.QUERY_PARAMS.get('start', None)
        end = self.request.QUERY_PARAMS.get('end', None)
        if start and end:
            queryset = queryset.filter(Q(start__gte=start) | Q(end__lte=end))
        return queryset


class BookingPriceAdminDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = BookingPrice.objects.all()
    serializer_class = BookingPriceAdminSerializer


class BookingPriceAdminList(generics.ListCreateAPIView):
    '''
    Only admins can create new calendar items
    '''
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminOrReadOnly,)
    serializer_class = BookingPriceAdminSerializer


    def get_queryset(self):
        """
        """
        queryset = BookingPrice.objects.all()
        last = self.request.QUERY_PARAMS.get('last', None)
        # if last is not given we'll return all items
        if last:
            # fetch the latest entry only
            queryset = [queryset.order_by('-end')[0:1].get()]
        return queryset


