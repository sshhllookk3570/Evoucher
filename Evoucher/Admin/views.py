from django.shortcuts import render,HttpResponse,redirect
from Voucher.models import Voucher
from Consumer.forms import ConsumerForm

# Create your views here.
def index(request):
    return  render(request,'Admin/adminhome.html')

def showvoucher(request):
    if request.method == 'POST':
        voucher=Voucher.objects.all()
        n = []
        for i in voucher:
            n.append({'code': i.code,
                  'face_value': i.face_value,
                  'Start_date': i.start_date,
                  'expriy_date': i.expiry_date}
                 )

    return HttpResponse(n)

def assign(request):
    return redirect('Admin/consumerform.html')


def assign_code(request):
    if request.method == "GET":
        form = ConsumerForm()
        return render(request, 'Admin/consumerform.html', {'form': form})

    if request.method == "POST":
        form = ConsumerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'Admin/stata.html', {'form': form})

    return render(request, 'Admin/status.html', {'form': form})
