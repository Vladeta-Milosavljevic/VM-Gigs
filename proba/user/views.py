from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User
from .helpers import send_registration_confirmation_email
from .custom_decorators import authentication_not_required
from django.utils.decorators import method_decorator




@authentication_not_required
def register(request):
    if (request.method == 'GET'):
        form = RegistrationForm()
        context = {
            'form': form
        }
        return render(request, 'user/register.html', context)

    elif (request.method == 'POST'):
        form = RegistrationForm(request.POST)

        if (form.is_valid()):
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            send_registration_confirmation_email(request, user)

            return redirect('login')
        else:
            context = {
                'form': form
            }
            return render(request, 'user/register.html', context)

@method_decorator(authentication_not_required, name='dispatch')
class ActivationView(View):
    def get(self, request, userId, token):
        try:
            id = urlsafe_base64_decode(userId).decode()
            user = User.objects.get(id=id)
        except Exception as error:
            pass
        if (user is None):
            context = {
                'error': "Invalid id"
            }
            return render(request, 'user/error.html', context)

        tokenGenerator = PasswordResetTokenGenerator()
        if (not tokenGenerator.check_token(user, token)):
            context = {
                'error': "Invalid token"
            }
            return render(request, 'user/error.html', context)

        user.is_active = True
        user.save()
        return redirect('login')
