from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from webapp.forms import PollForm, ChoiceForm
from webapp.models import Poll, Choice

class AnswerCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ChoiceForm()
        return render(request, 'create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text'],
                category=form.cleaned_data['category']
            )
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'create.html', context={'form': form})