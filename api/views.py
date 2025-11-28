from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet 

from .models import Item
from .serializers import ItemSerializer, FilterItemSerialer


class ItemsViewSet(ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()

        if self.action == 'list':
            filter_serializer = FilterItemSerialer(data=self.request.query_params)

            if filter_serializer.is_valid(raise_exception=True):
                status = filter_serializer.data.get('status')
                min_amount = filter_serializer.data.get('min_amount')
                max_amount = filter_serializer.data.get('max_amount')

                if status is not None:
                    queryset = queryset.filter(status=status)
                if min_amount is not None:
                    queryset = queryset.filter(amount__gte=min_amount)
                if max_amount is not None:
                    queryset = queryset.filter(amount__lte=max_amount)
        
        return queryset
    