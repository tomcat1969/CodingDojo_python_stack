from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('regist',views.regist),
    path('success',views.success),
    path('logout',views.logout),
    path('login',views.login)
]
