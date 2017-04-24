from django.shortcuts import render
from ranking.models import School, TestScores

def index(request):
    context = {}
    return render(request, 'ranking/homepage.html', context)


def schools_list(request):
    schools = School.objects.order_by('name')
    reading_scores = TestScores.objects.filter(test_type__type="NeSA Reading").order_by('school__name')
    context = {'schools': schools, 'reading_scores': reading_scores}
    return render(request, 'ranking/schools_list.html', context)

def schools_detail(request, pk):
    school = School.objects.get(id=pk)
    #reading_scores = TestScores.objects.filter(test_type__type="NeSA Reading").order_by('school__name')
    context = {'school': school}
    return render(request, 'ranking/schools_detail.html', context)
