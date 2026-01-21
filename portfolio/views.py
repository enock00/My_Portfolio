from django.shortcuts import render, redirect
from .models import Profile, Skill, Project, ContactMessage,WorkExperience

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = WorkExperience.objects.all()

    return render(request, 'portfolio/home.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
    })


def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        return redirect('home')

    return render(request, 'portfolio/contact.html')
