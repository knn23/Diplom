# forum/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Answer
from .forms import TopicForm, AnswerForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            #return redirect('forum:index')
    else:
        form = TopicForm()
    topics = Topic.objects.all().order_by('-created_at')
    return render(request, 'forum/index.html', {'form': form, 'topics': topics})

@login_required
def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    answers = Answer.objects.filter(topic=topic).order_by('-created_at')

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.topic = topic
            answer.author = request.user
            answer.save()
            #return redirect('forum:topic_detail', topic_id=topic_id)
    else:
        form = AnswerForm()

    return render(request, 'forum/answers.html', {'topic': topic, 'form': form, 'answers': answers})
