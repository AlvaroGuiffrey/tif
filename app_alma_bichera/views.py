from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView

from .models import Promo

# Create your views here.
class PromoBaseView:
    template_name = 'promociones.html'
    model = Promo
    fields = '__all__'
    success_url = reverse_lazy('promociones:all')

class PromoListView(PromoBaseView, ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS VINOS
    """

class PromoDetailView(PromoBaseView, DetailView):
    template_name = "vino_detail.html"

class PromoCreateView(PromoBaseView, CreateView):
    template_name = "promo_create.html"
    extra_context = {
        "tipo": "Crear promo"
    }

class PromoUpdateView(PromoBaseView, UpdateView):
    template_name = "promo_create.html"
    extra_context = {
        "tipo": "Actualizar promo"
    }   

class PromoDeleteView(PromoBaseView, DeleteView):
    template_name = "promo_delete.html"
    extra_context = {
        "tipo": "Borrar promo"
    }
