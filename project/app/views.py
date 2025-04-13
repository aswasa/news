from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import NewsCategory, News
from .forms import RegForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views import View



# Create your views here.
def home_page(request):
    categories=NewsCategory.objects.all()
    news=News.objects.all()

    context={'categories': categories, 'news': news}

    return render(request, 'home.html', context)

def category_page(request, pk):
    categories=NewsCategory.objects.get(id=pk)
    news=News.objects.filter(category=categories)


    context={'categories': categories, 'news': news}

    return render(request, 'category.html', context)

def news_page(request, pk):
    news=News.objects.get(id=pk)

    context={'news': news}

    return render(request, 'news.html', context)

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegForm}

        return render(request, self.template_name, context)


    def post(self, request):
        form = RegForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username=username,
                                     email=email,
                                     password=password)
            user.save()

            login(request, user)

        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')


