from django.urls import path
from . import views

app_name = "Operations"

urlpatterns = [
    path('',views.operations,name='operations'),
]