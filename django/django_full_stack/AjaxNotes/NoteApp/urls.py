from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addNote',views.addNote),
    path('feedbackNotes',views.feedbackNotes),
    path('delete/<int:note_id>',views.delete)

]
