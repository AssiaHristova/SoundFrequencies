from django.views import View


class AboutUsView(View):
    template_name = 'general/about_us.html'


class ContactUsView(View):
    template_name = 'general/contact_us.html'
