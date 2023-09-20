from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
import logging
from django.views.generic import TemplateView
from myapp.forms import UserForm, ManyFieldsForm
from myapp.models import User, Product

from myapp.models import Author, Post

logger = logging.getLogger(__name__)


def index(request):
    logger.info('index page access.')
    return HttpResponse("qq!")


def about(request):
    logger.debug('about page access.')
    return HttpResponse("about")


def year_post(request, year):
    text = ""

    return HttpResponse(f"Posts from {year} <br> {text}")


def post_detail(requset, year, mounth, slug):
    post = {
        "year": year,
        "mounts": mounth,
        "slug": slug,
        "title": "Кто быстрее стоздает списки",
        "content": "В процессе написания очередной программы задумался",
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp/index.html", context)


def view_for(request):
    my_list = ['apple', 'banana,', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'желтый',
        'знать': 'зеленый',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый'
    }
    context = {
        "my_list": my_list,
        "my_dict": my_dict
    }
    return render(request, 'myapp/for.html', context)


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp/post_full.html', {'post': post})


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            logger.info(f'Получили: {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'myapp/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsForm()
    return render(request, 'myapp/many_fields_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name} {email} {age}')
            user = User(name=name, email=email, password=password, age=age)
            user.save()
            message = 'Пользователь сохранен'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'myapp/user_form.html', {'form': form, 'message': message})


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее колличество в базе данных',
        'total': total,
    }
    return render(request, 'myapp/total_count.html', context)


def total_in_view(requsest):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее колличество посчитаное в представлении',
        'total': total
    }
    return render(requsest, 'myapp/total_count.html', context)


def total_in_template(request):
    context = {
        'title': 'Общее колличество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'myapp/total_count.html', context)


class MonthPost(View):
    def get(self, request, year, mounth):
        text = ""

        return HttpResponse(f"Post from {mounth}/{year}<br>{text}")


class HelloView(View):
    def get(self, request):
        logger.info('Hello page access.')
        return HttpResponse("Hello view")


class TemplIf(TemplateView):
    template_name = "myapp/if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 11
        return context
