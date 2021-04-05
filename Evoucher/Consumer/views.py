from django.shortcuts import render,redirect,HttpResponse
from .forms import ConsumervouchForm
from .models import Consumer
from Voucher.models import Voucher


def show( request):
    if request.method == "GET":
        form = ConsumervouchForm()
        return render(request, 'Consumer/vouchsearch.html', {'form': form})

    if request.method == "POST":
        try:
            form = ConsumervouchForm(request.POST)
            if form.is_valid():
                m=form.cleaned_data['mobile']
                cod=Consumer.objects.get(mobile=m).code
                vouch=Voucher.objects.get(code=cod)
                n=[]
                for i in vouch:
                    n.append({'code': i.code,
                              'face_value': i.face_value,
                              'Start_date': i.start_date,
                              'expriy_date': i.expiry_date}
                             )
                return HttpResponse(n)
        except:
            return render(request, 'Consumer/stata.html', {'form': form})

    #return render(request, 'Consumer/status.html', {'form': form})
