from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthUserModel(AbstractUser):
    def __str__(self):
        return self.username
    
class ProfileModel(models.Model):
    user=models.OneToOneField(AuthUserModel,on_delete=models.CASCADE,related_name='user_profile',null=True)
    profileimage=models.ImageField(upload_to='Media_file',null=True)
    DisplayName=models.CharField(max_length=200,null=True)
    mobile=models.PositiveIntegerField(null=True)
    Address=models.TextField(null=True)
    Occupation=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.DisplayName
    
class CashModel(models.Model):
    user=models.ForeignKey(AuthUserModel, on_delete=models.CASCADE,related_name='users_cash',null=True)
    source=models.CharField(max_length=200,null=True)
    datetime=models.DateTimeField(auto_now_add=True,null=True)
    amount=models.FloatField(null=True)
    description=models.TextField(null=True)
    def __str__(self):
        return self.source
    
class ExpenseModel(models.Model):
    user=models.ForeignKey(AuthUserModel, on_delete=models.CASCADE,related_name='users_expense',null=True)
    description=models.TextField(null=True)
    amount=models.FloatField(null=True)
    datetime=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.description
