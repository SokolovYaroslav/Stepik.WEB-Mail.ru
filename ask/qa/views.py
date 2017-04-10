from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from qa.models import Question, Answer
from django.http import HttpResponseRedirect, Http404
from qa.forms import AskForm, AnswerForm, SignUpForm, LoginForm

def index(request):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    questions = Question.objects.new()
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {
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
    user = request.user
    if user.is_authenticated():
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            form._user = request.user
            if form.is_valid():
                answer = form.save(question)
                url = answer.question.get_url()
                return HttpResponseRedirect(url)
        else:
            form = AnswerForm(initial = {
            'question' : q_id
            })
        return render(request, 'D_question.html', {
        'form': form,
        'question': question,
        'answers': answers,
        })
    else:
        return render(request, 'D_question_anon.html', {
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
    paginator.baseurl = '/popular/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'popular.html', {
    'title': 'Popular',
    'paginator': paginator,
    'questions': page.object_list,
    'page': page,
    })
def question_add(request):
    user = request.user
    if user.is_authenticated():
        if request.method == 'POST':
            form = AskForm(request.POST)
            form._user = request.user
            if form.is_valid():
                question = form.save()
                url = question.get_url()
                return HttpResponseRedirect(url)
        else:
            form = AskForm()
        return render(request,  'question_add.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
def mySignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,  user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def myLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form.is_valid()
        user = form.save()
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
