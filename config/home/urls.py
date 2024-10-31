from django.urls import path
from .views import homepage, detail

urlpatterns = [
    path('', homepage , name='homepage'),
    path('detail', detail, name='detail')
]