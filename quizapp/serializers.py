from rest_framework import serializers 
from .models import Student, Question, QuestionOption



class Student(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = ["id", "username", "score", "status"]



class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption 
        fields = ["id", "option", "is_correct"]


class QuestionSerializer(serializers.ModelSerializer):
    options = QuestionOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question 
        fields = ['id', 'question', 'options']