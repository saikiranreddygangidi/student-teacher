from django.db import models


class Student_questions(models.Model):
    id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=300)
    question_type = models.CharField(max_length=300)
    query=models.TextField(max_length=800)
    error_image=models.FileField(upload_to="pics")
    upload_on=models.DateField(auto_now=True)
    
    