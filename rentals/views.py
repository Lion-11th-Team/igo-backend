from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from rentals.models import Rental
from rentals.serializers import RentalListRetrieveSerializer


class RentalListRetrieveViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Rental.objects.filter(is_active=True)
    serializer_class = RentalListRetrieveSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=('POST',))
    def subscribe(self, request, *args, **kwargs):
        pass
