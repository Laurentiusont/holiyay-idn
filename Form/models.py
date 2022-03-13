from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class saran (models.Model):
    Nama        = models.CharField(max_length=255)
    isi         = models.TextField(max_length=255)
    publish		= models.DateTimeField(auto_now_add = True)
    update		= models.DateTimeField(auto_now = True)
    # slug		= models.SlugField(blank=True, editable = False)
    # def save(self):
    #     self.slug = slugify(self.Nama)
    #     super(saran, self).save()
    def get_absolute_url(self):
        return reverse('Form:list')
    def __str__(self):
        return "{}.{}".format(self.id, self.Nama)
