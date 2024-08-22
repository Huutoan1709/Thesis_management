from django.contrib import admin
from  kltn.models import *

# admin.site.register(Diem_TieuChi)

class CustomAdminSite(admin.AdminSite):
    site_header = "Quản trị khóa luận"
    site_title = "Trang quản trị"
    index_title = "Chào mừng đến với trang quản trị"

    def get_app_list(self, request, app_label=None):
        return super().get_app_list(request) + [
            {
                'name': 'BÁO CÁO THỐNG KÊ',
                'models': [
                    {
                        'name': 'Tần Suất Tham Gia Khóa Luận Của Các Khoa',
                        'admin_url': '/admin/thongketansuat/',
                        'view_only': True,
                    },
                    {
                        'name': 'Điểm Trung Bình Khóa Luận Các Khoa',
                        'admin_url': '/admin/thongkeavg/',
                        'view_only': True,
                    },
                ]
            }
        ]



# admin_site = CustomAdminSite(name='custom_admin')
#
#
#
# admin.site = admin_site








admin.site = CustomAdminSite(name='custom_admin')
admin.site.register(HoiDong)
admin.site.register(KhoaLuan_TieuChi)
admin.site.register(User)
admin.site.register(Khoa)
admin.site.register(TieuChi)
admin.site.register(ThanhVien_HoiDong)
admin.site.register(KhoaLuan)
