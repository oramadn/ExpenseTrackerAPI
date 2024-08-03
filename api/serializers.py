from rest_framework import serializers
from .models import User, Category, Expense, RecurringExpenseInstance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'role']
        extra_kwargs = {'password': {'write_only': True}}

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class RecurringExpenseInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringExpenseInstance
        fields = '__all__'