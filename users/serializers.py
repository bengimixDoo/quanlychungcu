from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Thêm thông tin tùy chỉnh vào token (ví dụ: username và role)
        token['username'] = user.username
        token['role'] = user.role

        return token