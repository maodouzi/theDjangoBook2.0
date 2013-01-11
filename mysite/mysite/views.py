from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render
from books.models import Publisher

def hello(request):
    return HttpResponse("Hello world")

my_homepage_view = hello

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', locals())

def first_app(request):
    publisher_list = Publisher.objects.all()
    return render(request, 'first_app.html', {'publisher_list': publisher_list})

def current_url_view_good(request):
    requestList = request.__dict__.items()
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return render(request, 'request_list.html', locals())

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render(request, 'search_form.html')


