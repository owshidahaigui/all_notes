from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def users(request):

    #c = request.COOKIES.get('username')
    request.session['username'] = 'guoxiaonao'
    # print(111111111)
    #request.session['username']
    # print(222222222)

    resp = HttpResponse('set cookie is ok')

    #resp.set_cookie('username', 'guoxiaonao', 60)
    return resp

def test_csrf(request):
    #csrf攻击网站

    return render(request, 'test_csrf.html')

def test_csrf_server(request):
    print('welcome to my bank~')
    print(request.GET.keys())
    print('Bey-Bey')
    return HttpResponse('bank api')


def test_xss(request):
    #s = request.POST.get('msg')
    #import html
    #s_a = html.escape(s)

    #s_a -> 数据库

    sc = '<script>alert(111)</script>'
    #sc_a = '&lt;script&gt;alert(111)&lt;/script&gt;'
    return render(request, 'test_xss.html', locals())
    #return HttpResponse(sc_a)










