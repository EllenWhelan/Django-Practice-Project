from django.shortcuts import render, get_object_or_404
from .models import Job
# Create your views here.
def ellen(request):
    jobs = Job.objects #gets job objects from JOb class into new variable
    return render(request,'jobs/home.html', {'jobs': jobs})#passing jobs to html file

def detail(request, job_id):
    #grabbing job basedon id from db or spit out 404
    job_detail=get_object_or_404(Job, pk=job_id) #prinary key=unique identifier of object
    return render(request,'jobs/detail.html', {'job':job_detail})
