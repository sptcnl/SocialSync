from django.urls import path
from .views import SignupView, LoginView

app_name = "accounts"

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
]