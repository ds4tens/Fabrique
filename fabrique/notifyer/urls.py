from django.urls import  path
from notifyer import views

urlpatterns = [
    path('client/', views.ClientApiView.as_view(), name='client'),
]
