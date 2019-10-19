from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from webapp.forms import PollForm, ChoiceForm
from webapp.models import Answer, Poll, Choice


class AnswerIndexView(View):
    def get(self, request, *args, **kwargs):
        poll = self.get_object()
        return render(request, 'answer/answer.html', {'poll': poll})

    def get_object(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)

    def post(self, request, *args, **kwargs):
        poll_id = kwargs.get('pk')
        choice_id = int(request.POST.get('answer'))
        poll = get_object_or_404(Poll, pk=poll_id)
        choice = get_object_or_404(Choice, pk=choice_id)
        answer = Answer()
        answer.poll = poll
        answer.choice = choice
        answer.save()
        return redirect('index')


#
#
# class AnswerView(View):
#     def get(self, request, *args, **kwargs):
#         poll = self.get_object()
#         return render(request, 'answer/answers.html', {'poll': poll})
#
#     def get_object(self):
#         poll_pk = self.kwargs.get('pk')
#         return get_object_or_404(Poll, pk=poll_pk)
#
#     def post(self, request, *args, **kwargs):
#         poll_id = kwargs.get('pk')
#         choice_id = int(request.POST.get('answer'))
#
#         pull = get_object_or_404(Poll, pk=poll_id)
#         choice = get_object_or_404(Choice, pk=choice_id)
#         answer = Answer()
#         answer.poll = pull
#         answer.choice = choice
#         answer.save()
#         return redirect('index')


# class AnswerCreateView(View):
#     def get(self, request, *args, **kwargs):
#         form = ChoiceForm()
#         return render(request, 'create.html', context={'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = ArticleForm(data=request.POST)
#         if form.is_valid():
#             article = Article.objects.create(
#                 title=form.cleaned_data['title'],
#                 author=form.cleaned_data['author'],
#                 text=form.cleaned_data['text'],
#                 category=form.cleaned_data['category']
#             )
#             return redirect('article_view', pk=article.pk)
#         else:
#             return render(request, 'create.html', context={'form': form})