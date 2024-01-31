from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django_ratelimit.decorators import ratelimit

from home.forms import FeedbackForm
from home.models import *


@method_decorator(ratelimit(key='ip', rate='1/m', method='POST'), name='post')
class IndexView(generic.CreateView):
    form_class = FeedbackForm
    template_name = 'index.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['galleries'] = Gallery.objects.all()
        context['persons'] = Person.objects.all()
        context['board_of_trustees'] = BoardOfTrustees.objects.all()
        context['feedbacks'] = Feedback.objects.all()
        context['contacts'] = Contacts.objects.all()
        return context

