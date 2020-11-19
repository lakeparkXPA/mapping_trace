from django.shortcuts import render
from map.models import Concept, Local

# Create your views here.

def concept_sql(request):
    result = Local.objects.all()

    return render(request, 'index.html', {'concept_result': result})

def test(request):


    return render(request, 'test.html')