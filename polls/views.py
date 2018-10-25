from django.shortcuts import render, get_object_or_404

from polls.models import Question


# Create your views here.
def index_view(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions_list': latest_questions_list}
    return render(request, 'index.html', context)


def detail_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'details.html', context)


def result_view(request, question_id):
    context = {'details': str(question_id)}
    return render(request, 'result.html', context)


def vote_view(request, question_id):
    context = {'details': str(question_id)}
    return render(request, 'vote.html', context)
