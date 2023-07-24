from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def send_registration_confirmation_email(request, user):
    currentSite = get_current_site(request)
    userId = user.id
    coddedUserId = urlsafe_base64_encode(force_bytes(userId))
    tokenGenerator = PasswordResetTokenGenerator()
    token = tokenGenerator.make_token(user)

    context = {
        'user': user,
        'domain': currentSite.domain,
        'userId': coddedUserId,
        'token': token,
    }

    body = render_to_string('user/email.html', context)
    email = EmailMessage(
        'Account activation',
        body,
        'admin@proba.com',
        [user.email]
    )
    email.send()