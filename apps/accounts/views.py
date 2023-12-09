from django.contrib.auth.views import LoginView as DefaultLoginView
from django.shortcuts import redirect, reverse
from django.views.generic import FormView


# Create your views here.
class LoginView(DefaultLoginView):
    template_name = 'pages/registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


class SignupView(FormView):
    template_name = 'pages/registration/login.html'

