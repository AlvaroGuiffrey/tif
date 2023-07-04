from django.views.generic import TemplateView

class LandingPage(TemplateView):
    template_name = "landing_page.html"
    extra_context = {
        "titulo" : "Página de Inicio"
    }
