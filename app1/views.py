from django.shortcuts import render
from.models import App1
# Create your views here.

def index(request):
    app1 = App1.objects.order_by('-pk')
    context={
        'app':app1,
    }
    return render(request, 'app1/index.html', context)