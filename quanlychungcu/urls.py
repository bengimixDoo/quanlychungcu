from django.contrib import admin
from django.urls import path, include

# Import view tùy chỉnh từ app 'users'
from users.views import MyTokenObtainPairView

# Vẫn import RefreshView như cũ
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # SỬA DÒNG NÀY:
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), # <-- DÙNG HÀNG TÙY CHỈNH

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('api.urls')),
]