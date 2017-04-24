from django.shortcuts import render
from ranking.models import School

def index(request):
    context = {}
    return render(request, 'ranking/homepage.html', context)


def schools_list(request):
    schools = School.objects.order_by('name')
    context = {'schools': schools}
    return render(request, 'ranking/schools_list.html', context)
