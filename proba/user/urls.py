from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import register, ActivationView


urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="user/login.html",
         next_page='jobs:index', redirect_authenticated_user=True), name="login"),
    path("logout/", LogoutView.as_view(template_name="user/logout.html"), name="logout"),
    path("activate/<userId>/<token>", ActivationView.as_view(), name="activation"),
    path('password_reset/', PasswordResetView.as_view(template_name="user/password_reset.html"), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"),
         name='password_reset_complete'),
]
