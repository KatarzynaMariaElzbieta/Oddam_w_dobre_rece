from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import Donation, Institution, User, Category
from .forms import NewUserForm, LoginForm

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
        categories = Category.objects.all()
        institution = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, 'institution': institution})


class Login(View):
    def get(self, request):
        form = LoginForm
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        ctx = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(username)
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_authenticated:
                    login(self.request, user)
                    ctx['user'] = user
                    return render(request, 'index.html', ctx)
            form = LoginForm()
            ctx['mess'] = "Błąd logowania. Spróbuj jeszcze raz."
            ctx['form'] = form
        return render(request, 'login.html', ctx)


def logout_view(request):
    logout(request)
    return redirect('login')


class Register(View):
    def get(self, request):
        form = NewUserForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = NewUserForm(request.POST)
        ctx = {'form': form}
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
            return redirect('login')
        message = 'Niepoprawne dane'
        return render(request, 'register.html', {'form': form, 'mess': message})
