from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'dashboard.html'

def start_search(request):
    return HttpResponse('entered text:' + request.POST['tag']+request.POST['start_date']+request.POST['end_date'])