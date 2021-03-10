from django.db import models

# Create your models here.

# https://egg-money.tistory.com/117 
# - 5번 과정 따라함. 필요에 따라 바꿀 것
class Keditalk(models.Model):
    text = models.TextField()