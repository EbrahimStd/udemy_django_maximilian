from django.urls import path
from . import views

urlpatterns = [
    path('<int:month>/', views.monthly_challenge_by_number), # int month selected
    path('<str:month>/', views.monthly_challenge), # string month selected
]
