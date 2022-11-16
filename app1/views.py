from django.shortcuts import render
from.models import App1
from django.db.models import Q
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

def search(request):#검색 
    search= App1.objects.all().order_by('-pk')
    q = request.POST.get('q')
    if q:
        search = search.filter(Q(title__icontains=q)|Q(content__icontains=q))
        
        return render(request, 'app1/search.html',{'search':search, 'q':q})
    else:
        return render(request, 'app1/search.html')