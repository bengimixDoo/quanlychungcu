# Mở file: users/views.py

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    """
    Sử dụng serializer tùy chỉnh của chúng ta
    """
    serializer_class = MyTokenObtainPairSerializer