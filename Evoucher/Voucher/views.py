from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import VoucherForm
from .models import Voucher
from django.views.generic import TemplateView




def get_data(request):

  if request.method =="GET":
        form = VoucherForm()
        return render(request, 'voucher/voucher.html', {'form': form})


  if request.method == "POST":
    form = VoucherForm(request.POST)
    if form.is_valid():
      form.save()
    else:
      return render(request, 'voucher/stata.html', {'form': form})

  return render(request, 'voucher/status.html', {'form': form})

"""class get_data():
    template_name='voucher/voucher.html'

    def get(self,request):
        form=VoucherForm()
        return render(request,self.template_name, {'form': form})

    def post(self,request):
        form=VoucherForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=VoucherForm()
            code = form.cleaned_data('code')
            face_value = form.cleaned_data('face_value')
            start_date = form.cleaned_data('start_date')
            expiry_date = form.cleaned_data('expiry_date')
            form= VoucherForm()
            return  redirect('voucher:voucher')

        #args={'form':form,'code':code,'face_value':face_value,'start_date':start_date,'expiry_date':expiry_date}
        return render(request,self.template_name,{'form':form})"""
