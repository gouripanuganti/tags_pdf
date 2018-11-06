from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Topic, Post
from .forms import NewTopicForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils import timezone
from .models import *
from .render import *
import requests
from threading import Thread, activeCount
from django.views.decorators.csrf import csrf_exempt


def home(request):
    boards = Board.objects.all()
    print(boards)
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    print(board)
    return render(request, 'topics.html', {'board': board})

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(message=form.cleaned_data.get('message'),
                                       topic = topic,
                                       created_by = user
                                       )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form' : form})


def send_email(file: list):
   pass

class Sale(View):
 
    def get(self, request):
        sales = Sales.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'sales': sales,
            'request': request
        }
        return render(request, 'pdf.html', params)

class Pdf(View):

    def get(self, request):
        sales = Sales.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'sales': sales,
            'request': request
        }
        return Render.render('pdf.html', params)

class PdfMail(View):

    def get(self, request):
        sales = Sales.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'sales': sales,
            'request': request
        }
        file = RenderToPdf.render_to_file('pdf.html', params)
        thread = Thread(target=send_email, args=(file,))
        thread.start()
        return HttpResponse("Processed")