from django.shortcuts import render
from.models import App1
# Create your views here.

def index(request):#괸리자 페이지 작성 내용
    index_contents = App1.objects.all()
    context={
        'index_contents':index_contents
    }
    return render(request, 'app1/index.html', context)

def detail(request, pk):#조회
    detail_contents = App1.objects.get(pk=pk)
    context={
        'detail_contents':detail_contents
    }
    return render(request, 'app1/detail.html', context)