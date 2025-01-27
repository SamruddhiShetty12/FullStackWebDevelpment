from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('page2.html/', views.page2,name='page2'),
    path('page3.html/', views.page3,name='page3'),
    path('page4.html/', views.page4,name='page4'),
    path('submit-contact/',views.submit_contact,name='submit_contact'),


]