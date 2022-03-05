from django.urls import path
from . import views

urlpatterns = [
    path('',views.displayCount, name="display-count"),
]
