from django.urls import path
from .views import helloview

urlpatterns = [
    path('', helloview, name='helloview' ),
]