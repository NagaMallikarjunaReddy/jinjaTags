from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'ram'}
    return render(request,'first.html',context=d)
