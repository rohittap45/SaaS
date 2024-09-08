from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def layout_page_view(request):
    return render(request, "base.html", {})


def home_page_view(request):
    queryset=PageVisit.objects.filter(path=request.path)
    PageVisit.objects.create(path=request.path)
    context={
        'pagevistis': queryset.count()
    }
    print(context)
    return render(request, "home.html", context)