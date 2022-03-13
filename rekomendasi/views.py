from django.views.generic.base import TemplateView
# Create your views here.


class index(TemplateView):
    template_name = 'rekomendasi/index.html'
    extra_context = {
        'Judul': 'Rekomendasi',
    }


class detail(TemplateView):
    template_name = 'rekomendasi/detail.html'
    extra_context = {
        'Judul': 'Detail',
    }
