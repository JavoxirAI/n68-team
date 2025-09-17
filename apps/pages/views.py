from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from apps.pages.forms import ContactForm
from apps.pages.models import AboutPageModel


class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactPageView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('pages:contact')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = []
        for key, value in form.errors.items():
            for error in value:
                errors.append(error)
        return self.render_to_response(self.get_context_data(errors=errors))


class NotFoundPageView(TemplateView):
    template_name = 'pages/404.html'


class AboutUsPageView(ListView):
    model = AboutPageModel
    template_name = 'pages/about-us.html'
    context_object_name = 'about'


class UserWishlistPageView(TemplateView):
    template_name = 'pages/user-wishlist.html'
