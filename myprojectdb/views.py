from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Student_questions
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Student_questions
        fields = ('student_name', 'question_type','query','error_image' )

def student_query(request):
    return render(request,"bench_consultant.html")
def student_questions(request):
    if request.method =='POST':
        form = ContactForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            form=ContactForm()
            return render(request,'bench_consultant.html',{'response':True,"form":form})
        else:
            return render(request,'bench_consultant.html',{'response':False})
        # student_name=request.POST['student_name']
        # question_type=request.POST['question_type']
        # query=request.POST['query']
        # image=request.POST['image']
        # data=Student_questions(student_name=student_name,question_type=question_type,query=query,image=image)
        # data.save();
    else:
        print("hello")
        form=ContactForm()
        return render(request,"bench_consultant.html",{'form':form})
def all_query(request):
    if request.method =='POST':
        q_types=request.POST['q-type']
        date=request.POST['date']
        if(len(q_types)>0 and len(date)>0):
            print("1")
            data=Student_questions.objects.filter(question_type=q_types,upload_on=date)
        elif(len(q_types)<=0):
            print("2")
            data=Student_questions.objects.filter(upload_on=date)
        elif(len(date)<=0):
            print("3")
            data=Student_questions.objects.filter(question_type=q_types)
        return render(request,"result_page.html",{"data":data})
    else:
        data=Student_questions.objects.all();
        return render(request,"result_page.html",{"data":data})
