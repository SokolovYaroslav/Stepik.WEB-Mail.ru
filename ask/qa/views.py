from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question, Answer
from django.http import HttpResponseRedirect, Http404

def index(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.new()[:]
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(request, 'index.html', {
    'title': 'Latests',
    'paginator': paginator,
    'questions': page.object_list,
    'page': page,
    })
def test(request, *args, **kwargs):
	return HttpResponse('OK')
def D_question(request, q_id):
    try:
        question = Question.objects.get(pk = q_id)
    except Question.DoesNotExist:
        raise Http404
    answers = Question.objects.get_answers(question)[:]
    return render(request, 'D_question.html', {
    'question': question,
    'answers': answers,
    })
def popular(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.popular()[:]
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    return render(request, 'popular.html', {
    'title': 'Popular',
    'paginator': paginator,
    'questions': page.object_list,
    'page': page,
    })
