from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from .gaze_tracker.example import Eye_duration


def showvideo(request):

    lastvideo = Video.objects.last()
    videofile = lastvideo.videofile

    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    path = videofile.path
    durations, offscreenduration = Eye_duration.output(path)

    context = {'videofile': videofile,
               'form': form,
               'duration': durations,
               'offscreenduration': offscreenduration
               }
    return render(request, 'Blog/videos.html', context)
