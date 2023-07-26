from django.urls import path
# from .import views
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('register/', register ,name='register'),
    path('login/', login ,name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('expenses/', expenses, name='expenses'),
    path('register_det/', register_det, name='user_reg'),
    path('daily/', daily_exp, name='daily'),
    path('monthly/',monthly_exp, name='monthly'),
    path('daily_plt/', chart_view_daily, name="daily_chart"),
    path('income/',income_f,name='income_f'),
]