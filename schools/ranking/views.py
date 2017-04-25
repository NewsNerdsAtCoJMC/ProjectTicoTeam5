from django.shortcuts import render
from ranking.models import School, TestScores, Statistics

def index(request):
    context = {}
    return render(request, 'ranking/homepage.html', context)


def schools_list(request):
    schools = School.objects.order_by('name')
    reading_scores = TestScores.objects.filter(test_type__type="NeSA Reading").order_by('school__name')
    writing_scores = TestScores.objects.filter(test_type__type="NeSA Writing").order_by('school__name')
    math_scores = TestScores.objects.filter(test_type__type="NeSA Math").order_by('school__name')
    science_scores = TestScores.objects.filter(test_type__type="NeSA Science").order_by('school__name')
    frlunch = Statistics.objects.filter(stat_type__type="Frlunch").order_by('school__name')
    gifted = Statistics.objects.filter(stat_type__type="Gifted").order_by('school__name')
    specialed = Statistics.objects.filter(stat_type__type="Specialed").order_by('school__name')


    context = {'schools': schools, 'reading_scores': reading_scores, 'writing_scores': writing_scores, 'math_scores': math_scores, 'science_scores': science_scores, 'frlunch': frlunch, 'gifted': gifted, 'specialed': specialed}
    return render(request, 'ranking/schools_list.html', context)



def schools_detail(request, pk):
    school = School.objects.get(id=pk)
    reading_score = TestScores.objects.filter(school=school).filter(test_type__type="NeSA Reading")
    math_score = TestScores.objects.filter(school=school).filter(test_type__type="NeSA Math")
    science_score = TestScores.objects.filter(school=school).filter(test_type__type="NeSA Science")
    writing_score = TestScores.objects.filter(school=school).filter(test_type__type="NeSA Writing")
    frlunch = Statistics.objects.filter(school=school).filter(stat_type__type="Frlunch")
    gifted = Statistics.objects.filter(school=school).filter(stat_type__type="Gifted")
    specialed = Statistics.objects.filter(school=school).filter(stat_type__type="Specialed")

    context = {'school': school, 'reading_score': reading_score, 'math_score': math_score, 'science_score': science_score, 'writing_score': writing_score}
    return render(request, 'ranking/schools_detail.html', context)
