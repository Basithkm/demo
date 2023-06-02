
# from django.core.exceptions import ValidationError
# from allauth.account.signals import user_signed_up
# from registration.models import Account

# def validate_phone_number(sender, request, user, **kwargs):
#     phone_number = user.phone_number
#     if Account.objects.filter(phone_number=phone_number).exclude(email=user.email).exists():
#         raise ValidationError('This phone number is already in use.')

