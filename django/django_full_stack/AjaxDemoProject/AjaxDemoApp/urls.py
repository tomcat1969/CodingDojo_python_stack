from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addPost',views.addPost),
    path('ajaxmessages', views.ajaxPost)

]
