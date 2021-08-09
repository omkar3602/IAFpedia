from django.db import models

# Create your models here.
class BlogPost(models.Model):
    day=models.CharField(max_length=20)
    date=models.DateField()
    title=models.CharField(max_length=1000)
    body=models.CharField(max_length=1000000)
    link=models.CharField(max_length=100)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class HistoricalEvent(models.Model):
    duration=models.CharField(max_length=50)
    title=models.CharField(max_length=1000)
    body=models.CharField(max_length=1000000)
    link=models.CharField(max_length=100)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class ArmyExam(models.Model):
    title=models.CharField(max_length=1000)
    language=models.CharField(max_length=50)
    occurance=models.CharField(max_length=50)
    mode_of_exam=models.CharField(max_length=50)
    eligibility_nationality=models.CharField(max_length=10000)
    eligibility_educational=models.CharField(max_length=10000)
    eligibility_age=models.CharField(max_length=500)
    link=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class NavyExam(models.Model):
    title=models.CharField(max_length=1000)
    language=models.CharField(max_length=50)
    occurance=models.CharField(max_length=50)
    mode_of_exam=models.CharField(max_length=50)
    eligibility_nationality=models.CharField(max_length=10000)
    eligibility_educational=models.CharField(max_length=10000)
    eligibility_age=models.CharField(max_length=500)
    link=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class AirforceExam(models.Model):
    title=models.CharField(max_length=1000)
    language=models.CharField(max_length=50)
    occurance=models.CharField(max_length=50)
    mode_of_exam=models.CharField(max_length=50)
    eligibility_nationality=models.CharField(max_length=10000)
    eligibility_educational=models.CharField(max_length=10000)
    eligibility_age=models.CharField(max_length=500)
    link=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    image=models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class ArmySyllabus(models.Model):
    title=models.CharField(max_length=1000)
    subjects=models.CharField(max_length=1000)
    syllabus=models.CharField(max_length=100000)
    
    def __str__(self):
        return self.title

class NavySyllabus(models.Model):
    title=models.CharField(max_length=1000)
    subjects=models.CharField(max_length=1000)
    syllabus=models.CharField(max_length=100000)
    
    def __str__(self):
        return self.title

class AirforceSyllabus(models.Model):
    title=models.CharField(max_length=1000)
    subjects=models.CharField(max_length=1000)
    syllabus=models.CharField(max_length=100000)
    
    def __str__(self):
        return self.title