from rest_framework import serializers
from .models import *


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class MortgageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortgage
        fields = '__all__'


class HomeValueEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeValueEstimator
        fields = '__all__'
