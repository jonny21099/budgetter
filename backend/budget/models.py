from django.db import models
from categories.models import Category
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Budget(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'category'], name='unique_user_category')
        ]
