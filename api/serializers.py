from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class FilterItemSerialer(serializers.Serializer):
    status = serializers.BooleanField(required=False)
    min_amount = serializers.FloatField(required=False)
    max_amount = serializers.FloatField(required=False)
