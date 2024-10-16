from rest_framework import generics

from .models import Slot
from .serializers import SlotSerializer

class SlotList(generics.ListCreateAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer


class SlotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

