from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview),
    path('count-list/', views.countList, name='count-list'),
    path('count-create/',views.countCreate, name="count-create"),
    # path('counter-detail/<str:pk>/', views.countDetail, name='counter-detail'),
    # path('counter-update/<str:pk>/',views.countUpdate, name='counter-update'),
    # path('api/counter-delete/<str:pk>/',views.countDelete, name='counter-delete'),
]
