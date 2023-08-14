from django.db import models

# Create your models here.
class Question(models.Model):
    # created a class called Question with the parameter of models.Model to use the models which was imported from django.db
    question_text = models.CharField(max_length=140)
    # created a question_text model with CharField method and made the max length of characters the user can enter 140
    date_published = models.DateTimeField()
    # created a date_published model with the DateTimeField method

class Choice(models.Model):
    # created a class called Choice with the parameter of models.Model to use the models which was imported from django.db
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # created a question model with the ForeignKey method with the Question parameter, which tells django that each choice is related to a single question
    # and to delete if this is not valid
    choice_text = models.CharField(max_length=140)
    # created a choice_text model with the CharField method and made the max length of characters the user can enter 140
    votes = models.IntegerField(default=0)
    # created a votes model with the IntegerField method and made the default of votes equal to 0

def __str__(self):
    return self.question_text, self.choice_text
    # created a string function to return the question_text and the choice_text as a string
