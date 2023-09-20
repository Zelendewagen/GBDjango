from django.urls import path
from .views import index, about, HelloView
from .views import year_post, MonthPost, post_detail
from .views import my_view
from .views import TemplIf, view_for
from .views import author_posts, post_full
from .views import user_form, many_fields_form, add_user
from .views import total_in_view, total_in_db, total_in_template

urlpatterns = [
    path('', my_view, name='index'),
    path('about/', about, name='about'),
    path('hello/', HelloView.as_view(), name='HELLO'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:mounth>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:mounth>/<slug:slug>/', post_detail, name='post_detail'),
    path('if/', TemplIf.as_view(), name='if'),
    path('for/', view_for, name='for'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full'),
    path('user/add/', user_form, name='user_form'),
    path('forms', many_fields_form, name='many_field_form'),
    path('add_user', add_user, name='add_user'),
    path('total_db/', total_in_db, name='db'),
    path('total_view/', total_in_view, name='view'),
    path('total_template/', total_in_template, name='template'),

]
