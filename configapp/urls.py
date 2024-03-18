from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('properties/', PropertyListCreateAPIView.as_view(), name='property'),
    path('agents/', AgentListCreateAPIView.as_view(), name='agent'),
    # path('mortgage/', MortgageViewSet.as_view(), name='mortgage'),
    path('home-value/', HomeValueEstimateCreateAPIView.as_view(), name='home'),
]

router = SimpleRouter()
router.register("", MortgageViewSet, basename='mortgage')
urlpatterns += router.urls
