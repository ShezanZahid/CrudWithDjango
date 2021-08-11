# from django.db.models.signals import post_save,pre_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.contrib.sites.shortcuts import get_current_site
# from .tokens import account_activation_token
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes,force_text


# @receiver(post_save,sender=User)
# def send_email(sender,instance,created,**kwargs):
#     if created:
        
#         user=instance
#         email_subject= 'Registration Varification Mail'

#         message = render_to_string('email_template.html', {
#                             'user': user,
#                             'domain':0,
#                             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                             'token': account_activation_token.make_token(user),
#                         })
#         send_mail(
#                 email_subject,
#                 message,
#                 'shezan.new@gmail.com',
#                 [user.email],
#                 fail_silently=False,
#             )
#         print("Working from Signal") 
           
            