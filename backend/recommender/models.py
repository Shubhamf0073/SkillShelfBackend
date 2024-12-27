from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    difficulty_level = models.CharField(max_length=50)
    course_rating = models.FloatField()
    course_url = models.URLField()
    course_description = models.TextField()
    skills = models.TextField()
    origin = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    link = models.URLField()
    about = models.TextField()
    school = models.CharField(max_length=100)
    rating = models.FloatField()
    description_word_count = models.IntegerField()
    about_length = models.IntegerField()
    course_description_length = models.IntegerField()
    difficulty_level_encoded = models.IntegerField()

    def __str__(self):
        return self.course_name