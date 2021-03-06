from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from webapp.models import Answer, Poll, Choice


class AnswerIndexView(View):
    def get(self, request, *args, **kwargs):
        poll = self.get_object()
        return render(request, 'answer/answer.html', {'poll': poll})

    def get_object(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=pk)
        choice_pk = int(request.POST.get("answer"))
        choice = get_object_or_404(Choice, pk=choice_pk)
        answer = Answer()
        answer.poll = poll
        answer.choice = choice
        answer.save()
        return redirect("index")


class StatisticsView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        poll = get_object_or_404(Poll, pk=pk)
        choices = poll.choices.all().values("pk")
