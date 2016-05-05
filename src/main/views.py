from django.shortcuts import render, render_to_response, redirect
from .models import Subject, Level, Video
from django.template import RequestContext

# Create your views here.


def level_list(request):
    context = {}
    levels = Level.objects.all()
    context['levels'] = levels
    return render(request, 'levels.html', context)


def subject_list(request):
    context = {}
    subjects = Subject.objects.all()
    context['subjects'] = subjects
    return render(request, 'subjects.html', context)


def subject_detail(request, pk):
    context = {}
    subject = Subject.objects.get(pk=pk)
    context['subject'] = subject
    return render(request, 'subject_detail.html', context)


def video_list(request):
    context = {}
    videos = Video.objects.all()
    context['videos'] = videos
    return render(request, 'video_list.html', context)

def video_view(request, pk):
    context = {}
   
    video = Video.objects.get(pk=pk)
    context['video'] = video
    


    return render(request, 'video_detail.html', context)    