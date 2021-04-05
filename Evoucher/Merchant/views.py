from django.shortcuts import render,HttpResponse
from .forms import MerchantForm
from Voucher.models import Voucher
from Consumer.models import Consumer

def redeem(request):
    if request.method == "GET":
        form = MerchantForm()
        return render(request, 'Merchant/Merchantredeem.html', {'form': form})

    if request.method == "POST":
        try:
            form = MerchantForm(request.POST)
            if form.is_valid():
                cod=form.cleaned_data['code']
                m=Consumer.objects.get(code=cod).mobile
                vouch=Voucher.objects.get(code=cod)
                n=[]
                n.append({'code': vouch.code,
                              'face_value': vouch.face_value,
                              'Start_date': vouch.start_date,
                              'expriy_date': vouch.expiry_date,
                              'mobile':m,
                          }
                             )
                return HttpResponse(n)
        except:
            return render(request, 'Merchant/stata.html', {'form': form})

