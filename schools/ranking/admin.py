from django.contrib import admin
from ranking.models import TestType, TestScores, School, Enrollment, ActivityType, Activities
# Register your models here.
admin.site.register(TestType)
admin.site.register(TestScores)
admin.site.register(School)
admin.site.register(Enrollment)
admin.site.register(ActivityType)
admin.site.register(Activities)
