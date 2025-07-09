from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer
from datetime import datetime

@api_view(['POST'])
def add_expense(request):
    data = request.data.copy()
    data['uid'] = request.firebase_user['uid']
    serializer = ExpenseSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_month_expenses(request):
    uid = request.firebase_user['uid']
    month_str = request.query_params.get('month')  # format: YYYY-MM
    try:
        year, month = map(int, month_str.split('-'))
    except:
        return Response({"error": "Invalid month format, use YYYY-MM"}, status=400)

    expenses = Expense.objects.filter(
        date__year=year,
        date__month=month,
        uid=uid
    )
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)

