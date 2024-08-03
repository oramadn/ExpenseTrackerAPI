from rest_framework import viewsets
from ..models import RecurringExpenseInstance
from ..serializers import RecurringExpenseInstanceSerializer

class RecurringExpenseInstanceViewSet(viewsets.ModelViewSet):
    queryset = RecurringExpenseInstance.objects.all()
    serializer_class = RecurringExpenseInstanceSerializer