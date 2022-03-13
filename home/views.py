from multiprocessing import context
from django.views.generic.base import TemplateView
# Create your views here.


class homeView(TemplateView):
    template_name = 'home/index.html'
    extra_context = {
        'Judul': 'Home',
    }
