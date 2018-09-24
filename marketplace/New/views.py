from django.views.generic import TemplateView, ListView



class HomePage(TemplateView):
    template_name = 'index.html'

class LoginSuccessPage(TemplateView):
    template_name = 'login_success.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
