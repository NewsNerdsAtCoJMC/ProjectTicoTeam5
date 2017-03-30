from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    description = models.TextField(null = True, blank = True)
    photo = models.ImageField(null = True, blank = True)
    def __str__(self):
        return self.name

class Enrollment(models.Model):
    school = models.ForeignKey(School)
    year = models.IntegerField()
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
class AreaCrime(models.Model):
     school = models.ForeignKey(School)
     year = models.DateField()
     rate = models.FloatField()

class ActivityType(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type

class Activities(models.Model):
    school = models.ForeignKey(School)
    acivity_type = models.ForeignKey(ActivityType)
    state_ranking = models.IntegerField()
    playoffs = models.CharField(max_length=255)
    record = models.CharField(max_length=255)
    year = models.DateField()
    size = models.CharField(max_length=255)

class Funding(models.Model):
    school = models.ForeignKey(School)
    amount = models.IntegerField()
