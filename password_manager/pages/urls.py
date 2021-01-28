from django.urls import path
from .views import homepage_view, welcome_page_view


urlpatterns = [
    path('', homepage_view, name="home"),
    path('welcome/', welcome_page_view, name="welcome"),
]