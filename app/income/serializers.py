from rest_framework import serializers
from .models import Income


class IncomeSerializer(serializers.ModelSerializer):
    """ Serializer for the Income model, in fields we specify the model attributes we want to deserialize and serialize """

    class Meta:
        model = Income
        fields = ['id', 'date', 'description', 'amount', 'source']
