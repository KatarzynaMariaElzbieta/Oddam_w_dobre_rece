from django.shortcuts import render
from django.views import View
from .models import Donation, Institution
# Create your views here.


class LandingPage(View):
    def get(self, request):
        dotations = Donation.objects.all()
        sum = 0
        for d in dotations:
            sum += d.quantity
        institutions = Institution.objects.all().count()
        ctx = {
            'sum_dotations': sum,
            'sum_institutions': institutions
        }
        return render(request, 'index.html', ctx)


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html', {})


class Login(View):
    def get(self, request):
        return render(request, 'login.html', {})


class Register(View):
    def get(self, request):
        return render(request, 'register.html', {})