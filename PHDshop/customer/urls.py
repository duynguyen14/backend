from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="homePage"),
    path('api/user/register/', views.CreateUserView.as_view(), name='create_user'),
    path('api/user/<int:pk>/update/', views.UpdateUserView.as_view(), name='update_user'),
    path('api/user/login/', views.LoginView.as_view(), name='login_user'),
]