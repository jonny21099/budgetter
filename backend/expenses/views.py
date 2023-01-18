from django.shortcuts import get_object_or_404
from rest_framework import generics
from expenses.models import Expense
from expenses.serializers import ExpenseSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field): # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

# Create your views here.
class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        expenses = Expense.objects.filter(user=self.kwargs.get('user'))
        category = self.request.query_params.get('category')
        if category is not None:
            expenses = expenses.filter(category=category)
        return expenses
    
    def perform_create(self, serializer):
        user = User.objects.get(username=self.kwargs.get('user'))
        serializer.save(user=user)
        
class ExpenseDetail(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_fields = ['user', 'name']
    
