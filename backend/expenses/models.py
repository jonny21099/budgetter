from django.db import models
from categories.models import Category
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Expense(models.Model):
    name = models.TextField()
    amount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
