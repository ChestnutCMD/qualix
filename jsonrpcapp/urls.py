from django.urls import path
from .views import jsonrpc_view

urlpatterns = [
    path('', jsonrpc_view, name='jsonrpc_view'),
]
