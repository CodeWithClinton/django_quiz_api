
from django.contrib import admin
from .models import Student, Question, QuestionOption

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'score', 'status')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)

@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('option', 'is_correct', 'question')
