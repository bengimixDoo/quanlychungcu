# Mở file: api/views.py
# (Xóa hết code cũ và dán code này vào)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    HoKhau, NhanKhau, PhiSinhHoat, PhiGuiXe,
    PhiDichVu, ThanhToan, CapNhatSinhHoat, TamTru, TamVang,
    PhiQuanLy, PhiDongGop, DSChiPhiDongGop
)
from .serializers import (
    HoKhauSerializer, NhanKhauSerializer, PhiSinhHoatSerializer,
    PhiGuiXeSerializer, PhiDichVuSerializer, ThanhToanSerializer,
    CapNhatSinhHoatSerializer, TamTruSerializer, TamVangSerializer,
    PhiQuanLySerializer, PhiDongGopSerializer, DSChiPhiDongGopSerializer
)

# API endpoint cho Hộ Khẩu
class HoKhauViewSet(viewsets.ModelViewSet):
    queryset = HoKhau.objects.all()
    serializer_class = HoKhauSerializer
    permission_classes = [IsAuthenticated] # Yêu cầu đăng nhập

# API endpoint cho Nhân Khẩu
class NhanKhauViewSet(viewsets.ModelViewSet):
    queryset = NhanKhau.objects.all()
    serializer_class = NhanKhauSerializer
    permission_classes = [IsAuthenticated]

# API endpoint cho Phí Sinh Hoạt
class PhiSinhHoatViewSet(viewsets.ModelViewSet):
    queryset = PhiSinhHoat.objects.all()
    serializer_class = PhiSinhHoatSerializer
    permission_classes = [IsAuthenticated]

# API endpoint cho Phí Gửi Xe
class PhiGuiXeViewSet(viewsets.ModelViewSet):
    queryset = PhiGuiXe.objects.all()
    serializer_class = PhiGuiXeSerializer
    permission_classes = [IsAuthenticated]

# API endpoint cho Phí Dịch Vụ
class PhiDichVuViewSet(viewsets.ModelViewSet):
    queryset = PhiDichVu.objects.all()
    serializer_class = PhiDichVuSerializer
    permission_classes = [IsAuthenticated]

# API endpoint cho Thanh Toán
class ThanhToanViewSet(viewsets.ModelViewSet):
    queryset = ThanhToan.objects.all()
    serializer_class = ThanhToanSerializer
    permission_classes = [IsAuthenticated]

# API endpoint cho Cập Nhật Sinh Hoạt
class CapNhatSinhHoatViewSet(viewsets.ModelViewSet):
    queryset = CapNhatSinhHoat.objects.all()
    serializer_class = CapNhatSinhHoatSerializer
    permission_classes = [IsAuthenticated]

# API endpoint cho Tạm Trú
class TamTruViewSet(viewsets.ModelViewSet):
    queryset = TamTru.objects.all()
    serializer_class = TamTruSerializer
    permission_classes = [IsAuthenticated]

# API endpoint cho Tạm Vắng
class TamVangViewSet(viewsets.ModelViewSet):
    queryset = TamVang.objects.all()
    serializer_class = TamVangSerializer
    permission_classes = [IsAuthenticated]

# API endpoint cho Phí Quản Lý
class PhiQuanLyViewSet(viewsets.ModelViewSet):
    queryset = PhiQuanLy.objects.all()
    serializer_class = PhiQuanLySerializer
    permission_classes = [IsAuthenticated]

# API endpoint cho Phí Đóng Góp
class PhiDongGopViewSet(viewsets.ModelViewSet):
    queryset = PhiDongGop.objects.all()
    serializer_class = PhiDongGopSerializer
    permission_classes = [IsAuthenticated]

# API endpoint cho Danh Sách Phí Đóng Góp
class DSChiPhiDongGopViewSet(viewsets.ModelViewSet):
    queryset = DSChiPhiDongGop.objects.all()
    serializer_class = DSChiPhiDongGopSerializer
    permission_classes = [IsAuthenticated]