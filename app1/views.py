from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):

    # return HttpResponse("hello")
    return render(request, "app1/base.html", context={
        "x" : 4, "y": 78,
    })