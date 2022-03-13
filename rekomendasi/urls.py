from django.urls import path
from .views import index, detail
app_name = 'rekomendasi'
urlpatterns = [
    path('', index.as_view(), name="rekomendasi"),
    path('detail', detail.as_view(), name="detail"),
]
