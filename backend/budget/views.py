from rest_framework import generics
from budget.serializers import BudgetSerializer
from budget.models import Budget
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

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

class BudgetList(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user=self.kwargs.get('user'))
    
    def perform_create(self, serializer):
        user = User.objects.get(username=self.kwargs.get('user'))
        serializer.save(user=user)

class BudgetDetail(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    lookup_fields = ['user', 'category']
