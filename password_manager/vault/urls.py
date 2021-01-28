from django.urls import path
from .views import (
    update_entry_view,
    delete_entry_view,
    create_entry_view,
    )

app_name = "entry"
urlpatterns = [
    path('create/', create_entry_view, name='create'),
    path('<int:entry_id>/edit/', update_entry_view, name="edit"),
    path('<int:entry_id>/delete/', delete_entry_view, name='delete'),
]