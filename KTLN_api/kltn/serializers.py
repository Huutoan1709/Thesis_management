from django.core.mail import send_mail
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *
from rest_framework import serializers
from django.db.models import Avg, Sum
from KTLN_api import  settings

class KhoaSerializer(ModelSerializer):
    class Meta:
        model = Khoa
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    def to_representation(self, instance):
        try:
            req = super().to_representation(instance)
            req['avt'] = instance.avt.url
        except:
            req['avt'] = None
        return req


class UserInfoSerializer(ItemSerializer):
    full_name = SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'email', 'chucvu', 'avt']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class ThanhVienHoiDongSerializer(ModelSerializer):
    class Meta:
        model = ThanhVien_HoiDong
        fields = ['vaitro']


class TieuChiSerializer(ModelSerializer):
    class Meta:
        model = TieuChi
        fields = ['ten']


class ThanhVienHoiDongDetailSerializer(ModelSerializer):
    class Meta:
        model = ThanhVien_HoiDong
        fields = ['id', 'vaitro']


class HoiDongSerializer(ModelSerializer):
    thanhviens = ThanhVienHoiDongSerializer(source='thanhvien_hoidong_set', many=True, read_only=True)
    trangthai = SerializerMethodField()

    class Meta:
        model = HoiDong
        fields = ['id', 'ten', 'trangthai', 'thanhviens']

    def get_trangthai(self, obj):
        has_true = False
        count = HoiDong.objects.get(pk=obj.id).thanhviens.count()

        if(HoiDong.objects.filter(id=obj.id, thanhvien_hoidong__vaitro='CHU TICH')\
            .filter(thanhvien_hoidong__vaitro='THU KY')\
            .filter(thanhvien_hoidong__vaitro='PHAN BIEN')\
            .exists() and count>=3):
            has_true = True
        else:
            has_true = False

        return has_true


class UserSerializer(ItemSerializer):

    def create(self, validated_data):

        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user_pass = validated_data.get('password',None)
        user = self.Meta.model(**validated_data)
        user.set_password(user_pass)
        user.save()

        subject = "Ho Chi Minh Open University"
        message = (f'Xin chào {user.last_name},\n Nhà trường cấp cho bạn tài khoản dùng để đăng nhập:\n username: {user.username} \n mật khẩu: {user_pass}'
                   f'\nSau khi đăng nhập hãy thay đổi để đảm bảo an toàn')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail(subject, message, email_from, recipient_list)

        return user

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'avt', 'chucvu']
        extra_kwargs = {
            'password': {
                'write_only': 'true'
            }
        }


class KhoaLuanInfoSerializer(ModelSerializer):
    class Meta:
        model = KhoaLuan
        fields = ['id','ten']


class ChiTietDiemSerializer(ModelSerializer):
    tieuchi = serializers.CharField()
    nguoi_danhgia = serializers.SerializerMethodField()
    class Meta:
        model = KhoaLuan_TieuChi
        fields = ['tieuchi', 'so_diem', 'nhanxet', 'nguoi_danhgia']

    def get_tieuchi(self, obj):
        return obj.tieuchi.ten
    def get_nguoi_danhgia(self, obj):
        return User.objects.get(pk=obj.nguoi_danhgia_id).username

class DiemSerializer(ModelSerializer):
    diems = ChiTietDiemSerializer(many=True, source='khoaluan_tieuchi_set')
    ten = serializers.CharField(read_only=True)
    total_score = serializers.SerializerMethodField()

    class Meta:
        model = KhoaLuan
        fields = ['ten', 'total_score', 'diems']

    def get_total_score(self, obj):
        total_score = obj.khoaluan_tieuchi_set.aggregate(sum_score=Avg('so_diem')).get('sum_score')
        return total_score



class User_KhoaLuanInfoSerializer(ModelSerializer):
    full_name = SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'email', 'chucvu', 'avt']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

class VaitroSerializer(serializers.Serializer):
    class Meta:
        model = serializers.CharField()

class TieuChiSerializer(ModelSerializer):
    class Meta:
        model = TieuChi
        fields = ['ten']

class KhoaLuanSerializer(ModelSerializer):
    sinhvien = User_KhoaLuanInfoSerializer(many=True)
    gv_huongdan = User_KhoaLuanInfoSerializer(many=True)
    hoidong = serializers.SerializerMethodField()
    khoa = KhoaSerializer()
    # tieuchis = TieuChiSerializer(many=True)
    giaovu = User_KhoaLuanInfoSerializer()

    class Meta:
        model = KhoaLuan
        fields = ('__all__')

    def get_hoidong(self, obj):
        TT_hoidong = HoiDongSerializer(obj.hoidong).data
        return TT_hoidong


class UserInfoWithRoleSerializer(ItemSerializer):
    full_name = SerializerMethodField()
    vaitro = SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'email', 'chucvu', 'avt', 'vaitro']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def get_vaitro(self, obj):
        hoidong_id = self.context.get('hoidong_id')
        print("serializer:", hoidong_id)
        thanhvien_hoidong = ThanhVien_HoiDong.objects.get(thanhvien=obj, hoidong_id=hoidong_id)
        if thanhvien_hoidong:
            return thanhvien_hoidong.get_vaitro_display()
        return None

###
class ThanhVien_HoiDongSerializer(ModelSerializer):
    hoidong_ten = serializers.CharField(source='hoidong.ten', read_only=True)
    class Meta:
        model = ThanhVien_HoiDong
        fields = ['hoidong','hoidong_ten', 'vaitro']

###
class TieuChiDetailSerializer(ModelSerializer):
    class Meta:
        model = TieuChi
        fields = '__all__'

class TieuChiNotIn(ModelSerializer):
    class Meta:
        model = TieuChi
        fields = '__all__'

class EmailSerializer(ModelSerializer):
    class Meta:
       model = User
       fields = ['email']

class UserNameAndId(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id']
