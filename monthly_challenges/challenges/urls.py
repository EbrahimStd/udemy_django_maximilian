from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('<int:month>/', views.monthly_challenge_by_number), # int month selected
    path('<str:month>/', views.monthly_challenge, name="challenge_month"), # string month selected
]
