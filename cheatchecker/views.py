from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from .gaze_tracker.example import Eye_duration


def showvideo(request):
    try:
        lastvideo = Video.objects.last()
        videofile = lastvideo.videofile

        form = VideoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

        path = videofile.path
        durations = Eye_duration.output(path)

        context = {'videofile': videofile,
                   'form': form,
                   'duration': durations
                   }
        return render(request, 'Blog/videos.html', context)
    except:
        print("starting")
