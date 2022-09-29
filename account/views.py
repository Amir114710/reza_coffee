from django.shortcuts import render , redirect , reverse
from django.views.generic import FormView , TemplateView , CreateView
from uuid import uuid4
from mixins import LoginRequirdMixins
from django.urls import reverse_lazy
from django.contrib.auth import login , authenticate , logout
import ghasedakpack
import requests
from .form import RegisterForm , OtpForm
from random import randint
from .models import OTP, User
SMS = ghasedakpack.Ghasedak("8534236d76060f342738a94b4ca72c")
class OtpRegisterationView(LoginRequirdMixins , FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home_app:home')
    def form_valid(self, form):
        cd = form.cleaned_data
        random_code = randint(1000 , 9999)
        SMS.verification({'receptor': cd['phone'] , 'type': '1','template': 'randcode','param1': random_code})
        token = str(uuid4())
        OTP.objects.create(phone = cd['phone'],code = random_code , token = token)
        print(random_code)
        return redirect(reverse('account:check_otp') + f'?token={token}')
class CheckOtpCode(FormView):
    template_name = 'account/otp_form.html'
    form_class = OtpForm
    success_url = reverse_lazy('home_app:home')
    def form_valid(self, form):
        token = self.request.GET.get('token')
        cd = form.cleaned_data
        if OTP.objects.filter(code=cd['code'],token=token).exists():
            otp = OTP.objects.get(token=token)
            user , is_created = User.objects.get_or_create(phone = otp.phone)
            login(self.request , user)
            otp.delete()
            return redirect('home_app:home')
        else:
            form.add_error(cd['code'] , 'this information is not correct')
        return render(self.request , self.template_name , {'form':form})
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home_app:home')
    else:
        return redirect('home_app:home')
