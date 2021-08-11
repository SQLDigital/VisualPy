from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('sendmail/', views.sendmail, name="sendmail"),
    path('apply/', views.apply, name="apply"),
    path('sendsurvey/', views.survey, name="sendsurvey"),

]