from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    """ Serializer for the Expense model, in fields we specify the model attributes we want to deserialize and serialize """
    class Meta:
        model = Expense
        fields = ['id', 'date', 'description', 'amount', 'category']
