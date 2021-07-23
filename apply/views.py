from django.shortcuts import render, get_object_or_404, redirect
from .models import Apply
from django.utils import timezone
from django.contrib import messages
# Create your views here.
def home(request):
    allblogs = Apply.objects.all()
    c = allblogs.count()
    return render(request, 'home.html', {'ablog':allblogs , 'count':c})

def detail(request, id):
    oneblog = get_object_or_404(Apply, pk = id)
    return render(request, 'detail.html', {'o':oneblog})

def new(request):
    return render(request, 'new.html')

def create(request):
    if Apply.objects.filter(snum = request.POST['csnum']).exists():
        eapply = get_object_or_404(Apply, snum = request.POST['csnum'])
        messages.info(request, '한 계정당 하나의 지원서만 작성 가능합니다!')
        return redirect('urldetail', eapply.id)
    cblog = Apply()
    cblog.name = request.POST['cname']
    cblog.snum = request.POST['csnum']
    cblog.dept = request.POST['cdept']
    cblog.motive = request.POST['cmotive']
    cblog.service = request.POST['cservice']
    cblog.saw = request.POST['csaw']
    cblog.aspire = request.POST['caspire']
    cblog.time = timezone.now()
    cblog.image = request.FILES.get('cimage')
    cblog.save()
    return redirect('urldetail', cblog.id)

def edit(request, id):
    eblog = Apply.objects.get(id = id)
    return render(request, 'edit.html', {'e':eblog})

def update(request, id):
    ublog = Apply.objects.get(id = id)
    ublog.name = request.POST['uname']
    ublog.snum = request.POST['usnum']
    ublog.dept = request.POST['udept']
    ublog.motive = request.POST['umotive']
    ublog.service = request.POST['uservice']
    ublog.saw = request.POST['usaw']
    ublog.aspire = request.POST['uaspire']
    ublog.time = timezone.now()
    ublog.image = request.FILES.get('uimage')
    ublog.save()
    return redirect('urldetail', ublog.id)

def delete(request, id):
    dblog = Apply.objects.get(id = id)
    dblog.delete()
    return redirect('urlhome')