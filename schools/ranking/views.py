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

def schools_list(request):
    schools = School.objects.order_by('name')
    writing_scores = TestScores.objects.filter(test_type__type="NeSA Writing").order_by('school__name')
    context = {'schools': schools, 'reading_scores': writing_scores}
    return render(request, 'ranking/schools_list.html', context)

def schools_list(request):
    schools = School.objects.order_by('name')
    math_scores = TestScores.objects.filter(test_type__type="NeSA Math").order_by('school__name')
    context = {'schools': schools, 'math_scores': math_scores}
    return render(request, 'ranking/schools_list.html', context)

def schools_list(request):
    schools = School.objects.order_by('name')
    science_scores = TestScores.objects.filter(test_type__type="NeSA Science").order_by('school__name')
    context = {'schools': schools, 'Science_scores': science_scores}
    return render(request, 'ranking/schools_list.html', context)

def schools_detail(request, pk):
    school = School.objects.get(id=pk)
    reading_score = TestScores.objects.filter(school=school).filter(test_type__type="NeSA Reading")
    math_score = TestScores.objects.filter(school=school).filter(test_type__type="NeSA Math")
    science_score = TestScores.objects.filter(school=school).filter(test_type__type="NeSA Science")
    writing_score = TestScores.objects.filter(school=school).filter(test_type__type="NeSA Writing")
    context = {'school': school, 'reading_score': reading_score, 'math_score': math_score, 'science_score': science_score, 'writing_score': writing_score}
    return render(request, 'ranking/schools_detail.html', context)
