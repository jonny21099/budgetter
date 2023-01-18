from django.urls import path
from .views import BudgetList, BudgetDetail

urlpatterns = [
    path('budget/', BudgetList.as_view()),
    path('budget/<str:category>', BudgetDetail.as_view())
]