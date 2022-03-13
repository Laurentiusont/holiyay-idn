from django.shortcuts import render
from .models import saran
from .forms import saranForm
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
# Create your views here.


class SaranUpdateView(UpdateView):
    form_class = saranForm
    model = saran
    template_name = 'form/create.html'

    extra_context = {
        'Judul': 'update Artikel dengan update view 1',
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)


class SaranDelete(DeleteView):
    model = saran
    template_name = 'form/saran_confirm_delete.html'
    success_url = reverse_lazy('Form:list')


class SaranView(CreateView):
    form_class = saranForm
    template_name = 'form/create.html'
    success_url = reverse_lazy('Form:list')
    extra_context = {
        'Judul': 'Tambah Saran',
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)
class SaranListView(ListView):
	model = saran
	# ordering = ['publish']
	# paginate_by = 2
	extra_context = {
		'Judul':'Saran List',
	}
	# def get_queryset(self):
	# 	if self.kwargs['nama'] != 'all':
	# 		self.queryset = self.model.objects.filter(Nama__iexact = self.kwargs['nama'])
	# 		self.kwargs.update({
	# 			'nama':self.kwargs['nama'],
	# 			})
	# 	return super().get_queryset()

	def get_context_data(self,*args,**kwargs):
		self.kwargs.update(self.extra_context)
		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)
