from django.urls import  path
from rest_framework.routers import DefaultRouter
from notifyer import views

router = DefaultRouter()
router.register(r'mailing', views.MailingViewSet, basename='mailingmodel')

urlpatterns = [
    path('client/', views.ClientApiView.as_view(), name='client'),
]+router.urls
