from django.shortcuts import render,HttpResponseRedirect
from .froms import Myform,userlogin,addform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Myblog,Contact
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    myblogs=Myblog.objects.all()
    return render(request,'home.html',{'blog':myblogs})
def about(request):
    return render(request,'about.html')

def save(request):
   if request.method=='POST':
      nm=request.POST.get('name')
      em=request.POST.get('email')
      msg=request.POST.get('message')
      con=Contact(name=nm,email=em,message=msg)
      con.save()
      # messages.success(request,'THANK YOU!')
   else:
      Contact()  
   return render(request,'contact.html',)


def contact(request):
    return render(request,'contact.html')
def mylogin(request):
  if not request.user.is_authenticated: 
    if request.method=='POST':
        lo=userlogin(request=request,data=request.POST)
        if lo.is_valid():
            un=lo.cleaned_data['username']
            pw=lo.cleaned_data['password']
            user= authenticate(username=un,password=pw)
            if user is not None:
             login(request,user)
             messages.success(request,'YOU ARE successfully LOGGED IN !!!')
             return HttpResponseRedirect('/dashboard/')
    else:       
      lo=userlogin()
    return render(request,'login.html',{'login':lo}) 
  else:
     return HttpResponseRedirect('/dashboard/') 
def mysignup(request):
    if request.method=='POST':
        fo=Myform(request.POST)
        if fo.is_valid():
            messages.success(request,'YOU ARE successfully SIGN IN ')
            user=fo.save()
            group=Group.objects.get(name='blogger')
            user.groups.add(group)
    else:       
     fo=Myform()
    return render(request,'signup.html',{'form':fo})


def dashboard(request):
    if request.user.is_authenticated: 
      blogs=Myblog.objects.all()
      user=request.user
      name=user.get_full_name()
      grps=user.groups.all()
      return render(request,'dashb.html',{'blog':blogs,'fullname':name,'groups':grps})
    else: 
     return HttpResponseRedirect('/login/')
    

def mylogout(request):
    logout(request)
    return HttpResponseRedirect('/')

def myupdate(request, id):
  if request.user.is_authenticated: 
   if request.method=='POST':
    upd=Myblog.objects.get(pk=id)
    myupd=addform(request.POST,instance=upd)
    if myupd.is_valid():
      myupd.save()  
   else:
      upd=Myblog.objects.get(pk=id)     
      myupd=addform(instance=upd)
   return render (request,'update.html',{'update':myupd})
  else:
     return HttpResponseRedirect('/login/')
  
def myadd(request):
  if request.user.is_authenticated: 
   if request.method=='POST':
      ad=addform(request.POST)
      if ad.is_valid():
         title=ad.cleaned_data['title']
         con=ad.cleaned_data['con']
         fo=Myblog(title=title,con=con) 
         fo.save()
         ad=addform()
   else:
      ad=addform()       
   return render (request,'add.html',{'add':ad})
  else:
     return HttpResponseRedirect('/login/') 
  
def mydelete(request ,id):
  if request.user.is_authenticated:
   if request.method=='POST':
    de=Myblog.objects.get(pk=id)
    de.delete()
   return HttpResponseRedirect('/dashboard/')  
  else:
     return HttpResponseRedirect('/login/') 