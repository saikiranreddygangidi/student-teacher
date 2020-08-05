from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.student_questions),
   
    path('student-questions',views.student_questions),
    path('all-query',views.all_query)
]