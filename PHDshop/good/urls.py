from django.urls import path
from .views import GoodListView
from .views import GoodDetailView
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('list', GoodListView.as_view(), name='good-list'),
    path('list/<int:id>/', GoodDetailView.as_view(), name='good-detail'),  # <int:id> captures the product ID
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Lấy access và refresh token
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # Làm mới access token
]