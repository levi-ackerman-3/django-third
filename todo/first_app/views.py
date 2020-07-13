from django.shortcuts import render
from first_app.models import todoadder
# Create your views here.
def firstpage(request):
    return render(request,"home.html")
def secondpage(request):
    if request.method=="POST":
        task=request.POST["task"]
        description=request.POST["description"]
        ins=todoadder(task=task,description=description)
        ins.save()
    return render(request,"todo.html")
def thirdpage(request):
    alltask=todoadder.objects.all()
    context={"tsk":alltask}
    return render(request,"list.html",context)
def delfun(request,slug):
    ins=todoadder.objects.filter(task=slug).first()
    ins.delete() 
    alltask=todoadder.objects.all()
    context={"tsk":alltask}
    return render(request,"list.html",context)