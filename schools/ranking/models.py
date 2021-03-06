from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    description = models.TextField(null = True, blank = True)
    photo = models.ImageField(upload_to="media", null=True, blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/schools/%s/" % self.id


class Enrollment(models.Model):
    school = models.ForeignKey(School)
    year = models.CharField(max_length=255)
    total_enrollment = models.IntegerField()

class TestType(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type

class TestScores(models.Model):
    school = models.ForeignKey(School)
    test_type = models.ForeignKey(TestType)
    below = models.FloatField()
    meeting = models.FloatField()
    exceeding = models.FloatField()
    def __str__(self):
        string = self.school.name + " " + self.test_type.type + " scores"
        return string

class ActivityType(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type

class Activities(models.Model):
    school = models.ForeignKey(School)
    acivity_type = models.ForeignKey(ActivityType)
    state_ranking = models.CharField(max_length=255)
    playoffs = models.CharField(max_length=255)
    record = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    size = models.CharField(max_length=255)

class StatType(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type

class Statistics(models.Model):
    school = models.ForeignKey(School)
    stat_type = models.ForeignKey(StatType)
    frlunch = models.CharField(max_length=225)
    gifted = models.CharField(max_length=225)
    specialed = models.CharField(max_length=225)
