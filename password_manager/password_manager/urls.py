from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('accounts.urls')),
    path('vault/', include('vault.urls')),

    # Password reset links
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='password_reset_templates/password_change_done.html'),
         name='password_change_done'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='password_reset_templates/password_change.html'),
         name='password_change'),
    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_templates/password_reset_confirm.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset_templates/password_reset_form.html'),
         name='password_reset'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_templates/password_reset_complete.html'),
         name='password_reset_complete'),
]
