# Mở file: quanlychungcu/urls.py

from django.contrib import admin
from django.urls import path, include

# Import view Token tùy chỉnh
from users.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # === URLs Đăng nhập (JWT) ===
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # (Chúng ta sẽ thêm 'api.urls' vào đây sau khi bạn sẵn sàng)
    # path('api/', include('api.urls')),
]