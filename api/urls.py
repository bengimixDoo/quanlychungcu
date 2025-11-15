# Mở file: api/urls.py
# (Xóa hết code cũ và dán code này vào)

from rest_framework.routers import DefaultRouter
from . import views

# DefaultRouter sẽ tự động tạo các URL cho chúng ta
router = DefaultRouter()

# Đăng ký các ViewSet (đã đồng bộ với models.py mới)
router.register(r'ho-khau', views.HoKhauViewSet, basename='hokhau')
router.register(r'nhan-khau', views.NhanKhauViewSet, basename='nhankhau')
router.register(r'phi-sinh-hoat', views.PhiSinhHoatViewSet, basename='phisinhhoat')
router.register(r'phi-gui-xe', views.PhiGuiXeViewSet, basename='phiguixe')
router.register(r'phi-dich-vu', views.PhiDichVuViewSet, basename='phidichvu')
router.register(r'thanh-toan', views.ThanhToanViewSet, basename='thanhtoan')
router.register(r'cap-nhat-sinh-hoat', views.CapNhatSinhHoatViewSet, basename='capnhatsinhhoat')
router.register(r'tam-tru', views.TamTruViewSet, basename='tamtru')
router.register(r'tam-vang', views.TamVangViewSet, basename='tamvang')
router.register(r'phi-quan-ly', views.PhiQuanLyViewSet, basename='phiquanly')
router.register(r'phi-dong-gop', views.PhiDongGopViewSet, basename='phidonggop')
router.register(r'ds-chi-phi-dong-gop', views.DSChiPhiDongGopViewSet, basename='dschiphidonggop')

# urlpatterns được router tự động tạo ra
urlpatterns = router.urls