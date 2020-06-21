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

        fund = Institution.objects.filter(type='fundacja')

        foundations = []
        for i in fund:
            foundations.append(i)

        op = Institution.objects.filter(type='organizacja_pozarzadowa')

        organizacja_pozarzadowa = []
        for i in op:
            organizacja_pozarzadowa.append(i)

        zl = Institution.objects.filter(type='zbiorka_lokalna')

        zbiorka_lokalna = []
        for i in zl:
            zbiorka_lokalna.append(i)

        ctx = {
            'sum_dotations': sum,
            'sum_institutions': institutions,
            'foundations': foundations,
            'organizacja_pozarzadowa': organizacja_pozarzadowa,
            'zbiorka_lokalna': zbiorka_lokalna,

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