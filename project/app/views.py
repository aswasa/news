from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import NewsCategory, News, Saves
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
    user_saves = Saves.objects.filter(user_id=request.user.id)

    context={'news': news, 'user_saves': user_saves}

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



def save(request, pk):
    if request.method == 'POST':
        news_item = News.objects.get(id=pk)
        existing_save = Saves.objects.filter(user_id=request.user.id, user_saves=news_item).first()

        if existing_save:
            existing_save.delete()
        else:
            Saves.objects.create(user_id=request.user.id, user_saves=news_item)
        return redirect('/')



def my_saves(request):
    user_saves = Saves.objects.filter(user_id=request.user.id)
    context = {'user_saves': user_saves}
    return render(request, 'save.html', context)

def delete_saves(request, pk):
    news_item = News.objects.get(id=pk)
    existing_save = Saves.objects.filter(user_id=request.user.id, user_saves=news_item).first()
    if existing_save:
        existing_save.delete()

    return redirect('/my_saves')





