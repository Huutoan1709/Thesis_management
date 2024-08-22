from rest_framework import permissions


class IsPermitUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_superuser == 1 or user.chucvu == 'GIAOVU' or user.chucvu == 'GIANGVIEN' or user.chucvu=='HOCSINH')


class IsPermitUserGivePoint(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_superuser == 1 or user.chucvu == 'GIANGVIEN')


class IsPermitMinistry(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_superuser == 1 or user.chucvu == 'GIAOVU')
