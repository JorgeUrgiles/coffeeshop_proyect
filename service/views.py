from django.shortcuts import render
from .models import Service

# Create your views here.
def service(request):
    services=Service.objects.all() #quieryset - consulta lista de servicios
    return render(request, "service/service.html", {'listServices':services})