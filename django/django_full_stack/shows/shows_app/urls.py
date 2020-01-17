from django.urls import path
from . import views
urlpatterns = [
    path('shows', views.AllShows),
    path('shows/new',views.new),
    path('shows/addnew',views.AddShow),
    path('', views.AllShows),
    path('shows/<str:show_id>/edit', views.editShow),
    path('shows/update',views.update),
    path('shows/<str:show_id>/detail',views.detail),
    path('shows/<str:show_id>/delete',views.delete)
]