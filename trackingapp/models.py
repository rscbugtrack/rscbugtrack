from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# from tinymce.models import HTMLField

# from ckeditor.fields import RichTextField

priority_choices = (('L','LOW'),('M','MEDIUM'),('H','HIGH'),)
current_status_choice= (('N','NotCompleted'),('O','Onprocess'),('C','Completed'),)

class Bugtrack(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    assigned_to = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    priority = models.CharField(max_length=2,choices=priority_choices)
    current_status = models.CharField(max_length=2,default='N',choices=current_status_choice)
    upload_image = models.ImageField(upload_to='butrackimg/',default='null')
    reference = models.CharField(max_length=40,default="Not Available")
    final_status = models.BooleanField(default=False)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

# yearsofexp = (('i','i',) for i in range(5))

database_choices= (('M','MySql'),('S','Sql'),('O','Oracle'),('Sq','Sqlite3'),('P','PostgreSQL'),)
class DevProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key_skills = models.CharField(max_length=100,help_text="Text your keyskil like python, Java or .net Developer")
    experience = models.PositiveIntegerField(default=0)
    programing_languages = models.CharField(max_length=100,help_text="List of progrming languages you know..")
    databases = models.CharField(max_length=2,choices=database_choices)
    designing = models.CharField(max_length=100,help_text="HTML, CSS, Bootstrap...etc")
    scripting = models.CharField(max_length=100,help_text="Javascript, Jquery, AngularJS..etc")
    tools = models.CharField(max_length=100,help_text="Like Pycharm, MySQL workbench...etc")

    # def __str__(self):
    #     return self.user





