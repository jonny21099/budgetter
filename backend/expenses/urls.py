from django.urls import path
from .views import ExpenseList, ExpenseDetail

urlpatterns = [
    path('expenses/', ExpenseList.as_view()),
    path('expenses/<str:name>', ExpenseDetail.as_view())
]