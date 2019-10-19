from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=5000, null=False, blank=False, verbose_name="Question")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Date created")

    def __str__(self):
        return self.question


class Choice(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Response text")
    poll = models.ForeignKey("webapp.Poll", related_name="choices", on_delete=models.CASCADE, verbose_name="Poll")

    def __str__(self):
        return self.text[:20]


class Answer(models.Model):
    poll = models.ForeignKey("webapp.Poll", related_name="answer_poll", on_delete=models.CASCADE, verbose_name="Poll")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    choice = models.ForeignKey("webapp.Choice", related_name="answer_choice", on_delete=models.CASCADE,
                               verbose_name="Choice")





