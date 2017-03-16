from django.contrib import admin
from ranking.models import TestType, TestScores, School
# Register your models here.
admin.site.register(TestType)
admin.site.register(TestScores)
admin.site.register(School)
