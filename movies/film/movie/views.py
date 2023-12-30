from django.shortcuts import render
from movie.models import Movie
from movie.forms import movieform
# Create your views here.
def home(request):
    b=Movie.objects.all()
    return render(request,'home.html',{'movie':b})
def add(request):
    if(request.method=="POST"):
        img=request.FILES['im']
        name=request.POST['n']
        des=request.POST['d']
        year=request.POST['ye']
        b=Movie.objects.create(image=img,name=name,description=des,year=year)
        b.save()
        return home(request)
    return render(request,'add.html')
def add1(request):
    form=movieform()
    if(request.method=="POST"):
        form=movieform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'add1.html',{'form':form})
def viewbyid(request,p):
    b=Movie.objects.get(id=p)
    return render(request,'view.html',{'m':b})
def delete(request,p):
    b=Movie.objects.get(id=p)
    b.delete()
    return home(request)
def update(request,p):
    b=Movie.objects.get(id=p)
    form=movieform(instance=b)
    if(request.method=="POST"):
        form=movieform(request.POST,request.FILES,instance=b)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'add1.html',{'form':form})
