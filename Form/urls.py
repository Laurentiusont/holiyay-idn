from django.urls import path,re_path
from .views import (
    SaranView,
    SaranUpdateView,
    SaranDelete,
    SaranListView

)

from .models import saran
from .forms import saranForm
app_name = 'Form'
urlpatterns = [
    path('',SaranListView.as_view(), name='list'),
    path('create/', SaranView.as_view(), name='create'),
    re_path('delete/(?P<pk>\d+)', SaranDelete.as_view(), name='delete'),
    re_path('update/(?P<pk>\d+)', SaranUpdateView.as_view(), name='update'),
]
