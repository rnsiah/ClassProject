from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import KitchnForm



class HomePageView(TemplateView):
    template_name = 'home.html'



def createkitchn(request):
    return render(request, 'createkitchn.html')


def startkitchn(request):
    return render(request, 'startkitchn.html',)



