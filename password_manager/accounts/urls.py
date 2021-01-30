from django.urls import path
from .views import (
    register_page_view, 
    login_page_view, 
    logout_view,
    account_page_view,
    must_authenticate_view,
    unauthorized_view,
)

app_name = "accounts"
urlpatterns = [
    # Account management links
    path('register/', register_page_view, name="register"),
    path('login/', login_page_view, name="login"),
    path('my-account/', account_page_view, name="account"),
    path('logout/', logout_view, name="logout"),
    path('must-authenticate/',must_authenticate_view, name="must_authenticate"),
    path('unauthorized/',unauthorized_view, name="unauthorized"),
]
