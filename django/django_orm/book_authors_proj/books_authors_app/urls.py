from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('books/<int:book_id>', views.showBook),
    path('addAuthor',views.addAuthor)
]