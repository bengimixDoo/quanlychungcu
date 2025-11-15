# Mở file: users/models.py
# (Xóa hết code cũ và dán code này vào)

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Model User tùy chỉnh, kế thừa từ User mặc định của Django.
    """

    # Định nghĩa các vai trò
    class Role(models.TextChoices):
        KE_TOAN = 'KE_TOAN', 'Kế toán'
        TO_TRUONG = 'TO_TRUONG', 'Tổ trưởng/Tổ phó'
        ADMIN = 'ADMIN', 'Quản trị viên'

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.ADMIN
    )

    # KHÔNG CÓ CLASS META
    # Bằng cách không khai báo "class Meta", chúng ta để Django tự do:
    # 1. Tự đặt tên bảng (sẽ là "users_customuser")
    # 2. Tự quản lý bảng (managed = True)