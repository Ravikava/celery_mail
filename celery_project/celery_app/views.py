from django.shortcuts import render
from .tasks import send_mail_task
from django.http import HttpResponse


# Create your views here.
def hello(request):
    try:
        text = "hello"
        send_mail_task.delay()
    except Exception as e:
        print("\n\n\n\n Error here: \n\n\n\n",e)
    return HttpResponse(text)


