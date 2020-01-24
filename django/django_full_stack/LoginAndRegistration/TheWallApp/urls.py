from django.urls import path
from . import views
urlpatterns = [
    path('', views.TheWallApp_index),
    path('postMessage',views.postMessage),
    path('postComment',views.postComment),
    path('deleteMessage',views.deleteMessage)
]
