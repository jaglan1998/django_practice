from django.shortcuts import render
import math
from . import models

# Create your views here.
def bgh(request):    
    return render(request, 'bgh.html')

def bgh_result(request):
    x = models.BaseGuideHours()
    x.sales_input = float(request.GET['sales'])
    x.ln_sales_input = float(request.GET['ln_sales'])
    lnh = x.cal_lnh
    bgh = x.cal_bgh   
    return render(request, 'bgh_result.html', {'lnh': lnh, 'bgh': bgh})