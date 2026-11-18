from django.urls import path,include
from .views import *

urlpatterns = [
    path('',AllStudent,name='all_student'),
    path('add/',AddStudent,name='add_student'),
    path('edit/<int:id>/',EditStudent,name='edit_student'),
    path('delete/<int:id>/',DeleteStudent,name='delete_student'),
]