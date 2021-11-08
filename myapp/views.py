from django.shortcuts import render,HttpResponse
from django.http import HttpResponse

# Create your views here.
from .tasks import sleepy,send_email_task

def home(request):
    if request.method=="POST":
        email=request.POST['email']
        
        send_email_task.delay(email)
        return HttpResponse('<h1>Thanks for feedback</h1>')

        
    return render(request,'myapp/index.html')
    
