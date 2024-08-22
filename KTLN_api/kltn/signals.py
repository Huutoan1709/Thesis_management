# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from .models import Hoidong_Giangvien, GiangVien
#
# @receiver(m2m_changed, sender=Hoidong_Giangvien.giangvien)
# def send_email_to_giangvien(sender, instance, action, pk_set, **kwargs):
#     if action == 'post_add':
#         giangvien_ids = list(pk_set)
#         for giangvien_id in giangvien_ids:
#             giangvien = GiangVien.objects.get(pk=giangvien_id)
#             subject = 'Thông báo: Bạn đã được thêm vào hội đồng'
#             message = 'Chào {},\n\nBạn đã được thêm vào hội đồng thành công.'.format(giangvien.username)
#             send_mail(subject, message, settings.EMAIL_HOST_USER, [giangvien.email])
