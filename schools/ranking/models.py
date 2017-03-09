from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(XXXXXXX)
    def __str__(self):
        return self.name

class Enrollment(models.Model):
    school = models.ForeignKey(School)
    year = models.DateField()
    total_enrollment = models.IntegerField()

class TestType(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type

class TestScores(models.Model):
    school = models.ForeignKey(School)
    test_type = models.ForeignKey(TestType)
    score = models.FloatField()

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
    year = models.DateField()

class Funding(models.Model):
    school = models.ForeignKey(School)
    amount = models.IntegerField()
