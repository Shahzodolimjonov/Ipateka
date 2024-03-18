from django.db import models


class Property(models.Model):
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    square_footage = models.PositiveIntegerField()
    photos = models.ImageField(upload_to='property_photos/')
    floor_plans = models.FileField(upload_to='floor_plans/')
    description = models.TextField()


class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class Mortgage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.FloatField()
    loan_term = models.PositiveIntegerField()


class HomeValueEstimator(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    estimated_value = models.DecimalField(max_digits=10, decimal_places=2)


