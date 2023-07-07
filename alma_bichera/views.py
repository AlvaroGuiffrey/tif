from django.views.generic import TemplateView

class LandingPage(TemplateView):
    template_name = "bloques/landing_page.html"
    extra_context = {
        "titulo" : "Alma Bichera"
    }

class ProductosPage(TemplateView):
    template_name = "bloques/productos.html"
    extra_context = {
        "titulo" : "Productos"
    }

class ConocenosPage(TemplateView):
    template_name = "bloques/conocenos.html"
    extra_context = {
        "titulo" : "Conocenos"
    }

class ContactoPage(TemplateView):
    template_name = "bloques/contacto.html"
    extra_context = {
        "titulo" : "Contacto"
    }
