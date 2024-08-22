from django.contrib import admin
from django.urls import path,re_path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('khoas', views.KhoaViewset, basename='khoas')
router.register('hoidongs', views.HoiDongViewset, basename='hoidongs')
router.register('users', views.UserViewset, basename='users')
router.register('hoidongdetail', views.HoiDongDetailViewset,basename='hoidongdetail')
router.register('khoa_khoaluans', views.Khoa_KhoaLuanViewset, basename='khoa_khoaluans')
router.register('diems', views.DiemViewset, basename='diems')
router.register('diem_detail', views.DiemDetailViewset, basename='diem_detail')
router.register('dskhoaluan', views.ListKhoaLuanViewSet, basename='dskhoaluan')
router.register('khoaluans', views.KhoaLuanViewset, basename='khoaluans')
router.register('tieuchis', views.TieuChiViewset, basename='tieuchis')
router.register('emails', views.EmailViewset, basename='emails')
router.register('suggests', views.UserInfoViewset, basename='suggest')
urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.home, name='home'),
    path('chitiet_diem/<int:id>/', views.diem_detail, name='diem_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/thongketansuat/', views.thong_ke_tan_suat, name='admin:thongketansuat'),
    path('admin/thongkeavg/', views.thong_ke_avg, name='admin:thongkeavg'),

]
