from django.contrib import admin
from ranking.models import TestType, TestScores, School, Enrollment
# Register your models here.
admin.site.register(TestType)
admin.site.register(TestScores)
admin.site.register(School)
admin.site.register(Enrollment)
