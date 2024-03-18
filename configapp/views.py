from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# GET,POST AND FILTER,SEARCH
class PropertyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["location"]
    search_fields = ["location", "price", "square_footage"]


# GET,POST
class AgentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class MortgageViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = MortgageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        down_payment = serializer.validated_data['down_payment']
        interest_rate = serializer.validated_data['interest_rate']
        years = serializer.validated_data['years']
        property_price = serializer.validated_data['property'].price
        monthly_payment = self.calculate_mortgage(property_price, down_payment, interest_rate, years)
        return Response({'monthly_payment': monthly_payment})

    def calculate_mortgage(self, property_price, down_payment, interest_rate, years):
        # Bu oylik ipoteka to'lovini hisoblash uchun formula
        loan_amount = property_price - down_payment
        monthly_interest_rate = interest_rate / 12 / 100
        total_payments = years * 12
        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)
        return monthly_payment


# GET,POST
class HomeValueEstimateCreateAPIView(generics.CreateAPIView):
    queryset = HomeValueEstimator.objects.all()
    serializer_class = HomeValueEstimateSerializer



