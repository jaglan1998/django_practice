from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'sign_board.html')

def sign_board(request):

    # user inputs
    what_to_write = request.GET['for_board'].upper()
    what_is_written = request.GET['on_board'].upper()
    
    all_letters_need = [i for i in what_to_write if i != ' ']
    all_letters_have = [i for i in what_is_written if i != ' ']
    
    
    def get_freq(lst):
        f = {}
        for i in lst:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        return f
    
    
    # print(get_freq(all_letters_need))
    # print(get_freq(all_letters_have))
    
    A = get_freq(all_letters_need)
    B = get_freq(all_letters_have)
    
    for k, v in A.items():
        if k in B.keys():
            # print(k, ' ', v)
            A[k] = v - B[k]
    
    res = {}

    for k, v in A.items():
        if v > 0:
            # print(f'{k} ---> {v}')
            res[k] = v
            
    print(res)
    return render(request, 'sign_result.html', {'result': res})   