from django.contrib import admin
# imported admin from django.contrib
from .models import Question, Choice
# imported the Question and Choice classes which was made in the .models project

# Register your models here.
admin.site.register(Question)
# used admin with the .site method and registered the Question class
admin.site.register(Choice)
# used admin with the .site method and registered the Choice class
