from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)

@login_required
def userProfile(request):
    user = request.user
    context = {'user':user}
    template = 'profile.html'
    return render(request, template, context)


