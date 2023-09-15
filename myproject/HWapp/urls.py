from django.urls import path
from HWapp.views import index, about, sorted_on_date
from HWapp.views import sorted_on_week, sorted_on_month, sorted_on_year
from HWapp.views import upload_image

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('client/<int:client_id>/', sorted_on_date, name='sorted_on_date'),

    path('by_week/<int:client_id>/', sorted_on_week, name='sorted_on_week'),
    path('by_month/<int:client_id>/', sorted_on_month, name='sorted_on_month'),
    path('by_year/<int:client_id>/', sorted_on_year, name='sorted_on_year'),

    path('upload_image', upload_image, name='upload_image'),
]
