from django.shortcuts import render

# Create your views here.
def hello(request):
    d={'name':'siddhu','age':23,'num':[12,52,30,82]}
    return render(request,'hello.html',context=d)


def hii(request):
    d={'a':20,'b':30,'c':'karthik','e':['karthik','siddhu','mahesh']}
    return render(request,'hii.html',context=d)