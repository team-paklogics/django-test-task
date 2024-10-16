from django.urls import path
from .views import SlotDetail, SlotList

urlpatterns = [
    path('slot/', SlotList.as_view()),
    path('slot/<int:pk>/', SlotDetail.as_view()),
]
