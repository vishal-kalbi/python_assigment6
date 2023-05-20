from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',CreateData.as_view(), name='create_data'),
    path('get_data/<int:pk>',GetData.as_view(), name='get_data'),
    path('update_data/<int:pk>',UpdateData.as_view(), name='update_data'),
    path('delete_data/<int:pk>',DeleteData.as_view(), name='delete_data')
]


