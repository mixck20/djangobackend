from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/register/', views.register_user, name='register_user'),
    path('api/login/', views.login_user, name='login_user'),
    path('api/profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]