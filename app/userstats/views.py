from django.shortcuts import render
from rest_framework.views import APIView
import datetime
from expenses.models import Expense
from rest_framework import status, response


class ExpenseSummaryStats(APIView):

    def get_amount_for_category(self, expence_list, category):
        expences=expence_list.filter(category=category)
        amount = 0

        for expence in expences:
            amount+=expence.amount

        return {'amount': str(amount)}

    def get_category(self, expence):
        return expence.category

    def get(self, request):
        todays_date = datetime.date.today()
        year_ago = todays_date-datetime.timedelta(days=365)
        expences = Expence.objects.filter(owner=request.user, date__gte=year_ago, date__lte=todays_date)
        final = {}
        category = list(set(map(self.get_category, expences)))

        for expence in expences:
            for category in categories:
                final[category] = self.get_amount_for_category(expences, category)

        return response.Response({'category_data': final}, status=status.HTTP_200_OK)
