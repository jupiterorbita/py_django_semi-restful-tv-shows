from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows', views.shows),
    path('shows/new', views.shows_new),
    path('create', views.create),
    path('show/<int:show_id>', views.show),
    path('show/<int:show_id>/edit', views.edit),
    path('show/<int:show_id>/update', views.update),
    path('shows/<int:show_id>/destroy', views.destroy)
]
