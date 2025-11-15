# Mở file: api/serializers.py
# (Xóa hết code cũ và dán code này vào)

from rest_framework import serializers
from .models import (
    HoKhau, NhanKhau, PhiSinhHoat, PhiGuiXe,
    PhiDichVu, ThanhToan, CapNhatSinhHoat, TamTru, TamVang,
    PhiQuanLy, PhiDongGop, DSChiPhiDongGop
)
# LƯU Ý: Không import 'Users' vì nó nằm ở app 'users'
# LƯU Ý: Không import 'KhoanThu' hay 'NopTien' vì chúng không còn tồn tại

class HoKhauSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoKhau
        fields = '__all__'

class NhanKhauSerializer(serializers.ModelSerializer):
    class Meta:
        model = NhanKhau
        fields = '__all__'

class PhiSinhHoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhiSinhHoat
        fields = '__all__'

class PhiGuiXeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhiGuiXe
        fields = '__all__'

class PhiDichVuSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhiDichVu
        fields = '__all__'

class ThanhToanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThanhToan
        fields = '__all__'

class CapNhatSinhHoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapNhatSinhHoat
        fields = '__all__'

class TamTruSerializer(serializers.ModelSerializer):
    class Meta:
        model = TamTru
        fields = '__all__'

class TamVangSerializer(serializers.ModelSerializer):
    class Meta:
        model = TamVang
        fields = '__all__'

class PhiQuanLySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhiQuanLy
        fields = '__all__'

class PhiDongGopSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhiDongGop
        fields = '__all__'

class DSChiPhiDongGopSerializer(serializers.ModelSerializer):
    class Meta:
        model = DSChiPhiDongGop
        fields = '__all__'