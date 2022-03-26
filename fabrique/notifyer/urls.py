from django.urls import  path
from rest_framework.routers import DefaultRouter
from notifyer import views

router = DefaultRouter()
router.register(r'mailing', views.MailingViewSet, basename='mailingmodel')
router.register(r'client', views.ClientViewSet, basename='client')

urlpatterns = [
    path('message/group/', views.MessageToMailingStatView.as_view(), name='message_to_mailing'),
    path('message/stats/', views.MessageStatView.as_view(), name='message_stat'),
    path('message/list/', views.MessageAllView.as_view(), name='message_all'),
]+router.urls
