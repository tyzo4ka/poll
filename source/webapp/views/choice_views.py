from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from webapp.forms import ChoiceForm, PollChoiceForm
from webapp.models import Choice, Poll


class ChoiceListView(ListView):
    context_object_name = 'choices'
    model = Choice
    template_name = 'choice/list.html'
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 3


class ChoiceForPollCreateView(CreateView):
    template_name = 'choice/create.html'
    form_class = PollChoiceForm

    def form_valid(self, form):
        poll_pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=poll_pk)
        poll.choices.create(**form.cleaned_data)
        return redirect('poll_view', pk=poll_pk)


class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'choice/create.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/update.html'
    form_class = PollChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})
