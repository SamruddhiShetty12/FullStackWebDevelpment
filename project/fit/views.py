from django.shortcuts import render
from .models import fit
from .forms import fitForm
from django.shortcuts import get_object_or_404,redirect
# Create your views here.
def index(request):
    return render(request,'index.html')
def page2(request):
     return render(request,'page2.html')
def page3(request):
     return render(request,'page3.html')
def page4(request):
     return render(request,'page4.html')
def submit_contact(request):
     if request.method=='POST':
          form=fitForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('page4')
          else:
               form=fitForm()
               return render(request,'page2.html',{'form':form})


     
     
        
    
        

        

