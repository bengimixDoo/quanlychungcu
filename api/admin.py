# Mở file: api/admin.py
# (Xóa hết code cũ và dán code này vào)

from django.contrib import admin
from .models import (
    HoKhau, NhanKhau, PhiSinhHoat, PhiGuiXe,
    PhiDichVu, ThanhToan, CapNhatSinhHoat, TamTru, TamVang,
    PhiQuanLy, PhiDongGop, DSChiPhiDongGop
)
# LƯU Ý: Chúng ta đã XÓA 'Users' khỏi danh sách import này

@admin.register(HoKhau)
class HoKhauAdmin(admin.ModelAdmin):
    list_display = ('mahokhau', 'diachi', 'ngaylap', 'dientichho')
    search_fields = ('mahokhau', 'diachi')

@admin.register(NhanKhau)
class NhanKhauAdmin(admin.ModelAdmin):
    list_display = ('hoten', 'socccd', 'mahokhau', 'gioitinh', 'sodt', 'quanhe')
    search_fields = ('hoten', 'socccd', 'mahokhau')
    list_filter = ('gioitinh', 'quanhe')

@admin.register(TamTru)
class TamTruAdmin(admin.ModelAdmin):
    list_display = ('socccd', 'tu_ngay', 'den_ngay', 'ly_do')
    search_fields = ('socccd',)

@admin.register(TamVang)
class TamVangAdmin(admin.ModelAdmin):
    list_display = ('socccd', 'tu_ngay', 'den_ngay', 'noi_tam_tru')
    search_fields = ('socccd',)

# Đăng ký các model về Phí (hiển thị cơ bản)
admin.site.register(PhiSinhHoat)
admin.site.register(PhiGuiXe)
admin.site.register(PhiDichVu)
admin.site.register(PhiQuanLy)
admin.site.register(PhiDongGop)
admin.site.register(DSChiPhiDongGop)

# Đăng ký các model còn lại
admin.site.register(ThanhToan)
admin.site.register(CapNhatSinhHoat)